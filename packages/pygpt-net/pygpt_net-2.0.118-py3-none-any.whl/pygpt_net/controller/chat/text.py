#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ================================================== #
# This file is a part of PYGPT package               #
# Website: https://pygpt.net                         #
# GitHub:  https://github.com/szczyglis-dev/py-gpt   #
# MIT License                                        #
# Created By  : Marcin Szczygliński                  #
# Updated Date: 2024.01.24 18:00:00                  #
# ================================================== #

from PySide6.QtWidgets import QApplication

from pygpt_net.item.ctx import CtxItem
from pygpt_net.core.dispatcher import Event
from pygpt_net.utils import trans


class Text:
    def __init__(self, window=None):
        """
        Text input controller

        :param window: Window instance
        """
        self.window = window

    def send(
            self,
            text: str,
            internal: bool = False
    ) -> CtxItem:
        """
        Send text message

        :param text: text to send
        :param internal: internal call
        :return: context item
        """
        self.window.ui.status(trans('status.sending'))

        # prepare names
        self.log("User name: {}".format(self.window.core.config.get('user_name')))  # log
        self.log("AI name: {}".format(self.window.core.config.get('ai_name')))  # log

        # event: username prepare
        event = Event(Event.USER_NAME, {
            'value': self.window.core.config.get('user_name'),
        })
        self.window.core.dispatcher.dispatch(event)
        user_name = event.data['value']

        # event: ai.name
        event = Event(Event.AI_NAME, {
            'value': self.window.core.config.get('ai_name'),
        })
        self.window.core.dispatcher.dispatch(event)
        ai_name = event.data['value']

        self.log("User name [after plugin: user_name]: {}".format(user_name))  # log
        self.log("AI name [after plugin: ai_name]: {}".format(ai_name))  # log

        # get mode
        mode = self.window.core.config.get('mode')
        model = self.window.core.config.get('model')
        model_data = self.window.core.models.get(model)

        # create ctx item
        ctx = CtxItem()
        ctx.internal = internal
        ctx.current = True  # mark as current context item
        ctx.mode = mode  # store current selected mode (not inline changed)
        ctx.model = model  # store model list key, not real model id
        ctx.set_input(text, user_name)
        ctx.set_output(None, ai_name)

        # upload assistant attachments (only assistant mode here)
        attachments = self.window.controller.chat.files.upload(mode)
        if len(attachments) > 0:
            ctx.attachments = attachments

        # store history (input)
        if self.window.core.config.get('store_history'):
            self.window.core.history.append(ctx, "input")

        # store thread id, assistant id and pass to gpt wrapper
        if mode == 'assistant':
            self.window.controller.assistant.prepare()  # create new thread if not exists
            ctx.thread = self.window.core.config.get('assistant_thread')

        # log
        self.log("Context: input: {}".format(self.window.core.ctx.dump(ctx)))

        # event: context before
        event = Event(Event.CTX_BEFORE)
        event.ctx = ctx
        self.window.core.dispatcher.dispatch(event)

        # log
        self.log("Context: input [after plugin: ctx.before]: {}".
                 format(self.window.core.ctx.dump(ctx)))
        self.log("System: {}".format(self.window.core.gpt.system_prompt))

        # event: prepare prompt (replace system prompt)
        sys_prompt = self.window.core.config.get('prompt')
        event = Event(Event.PRE_PROMPT, {
            'mode': mode,
            'value': sys_prompt,
        })
        self.window.core.dispatcher.dispatch(event)
        sys_prompt = event.data['value']

        # event: system prompt (append to system prompt)
        event = Event(Event.SYSTEM_PROMPT, {
            'mode': mode,
            'value': sys_prompt,
        })
        self.window.core.dispatcher.dispatch(event)
        sys_prompt = event.data['value']

        # event: post prompt (post-handle system prompt)
        event = Event(Event.POST_PROMPT, {
            'mode': mode,
            'value': sys_prompt,
        })
        event.ctx = ctx
        self.window.core.dispatcher.dispatch(event)
        sys_prompt = event.data['value']

        # event: command syntax apply (if commands enabled then append commands prompt)
        if self.window.core.config.get('cmd'):
            sys_prompt += " " + self.window.core.command.get_prompt()
            data = {
                'mode': mode,
                'prompt': sys_prompt,
                'syntax': [],
            }
            event = Event(Event.CMD_SYNTAX, data)
            self.window.core.dispatcher.dispatch(event)
            sys_prompt = self.window.core.command.append_syntax(event.data)

        # log
        self.log("System [after plugin: system.prompt]: {}".format(sys_prompt))
        self.log("User name: {}".format(ctx.input_name))
        self.log("AI name: {}".format(ctx.output_name))
        self.log("Appending input to chat window...")

        # stream mode
        stream_mode = self.window.core.config.get('stream')

        # render: begin
        self.window.controller.chat.render.begin(stream=stream_mode)

        # append text from input to chat window
        self.window.controller.chat.render.append_input(ctx)

        # add ctx to DB here and only update it after response,
        # MUST BE REMOVED NEXT AS FIRST MSG (LAST ON LIST)
        self.window.core.ctx.add(ctx)

        # update ctx list, but not reload all to prevent focus out on lists
        self.window.controller.ctx.update(reload=True, all=False)

        # process events to update UI
        QApplication.processEvents()

        try:
            # make API call
            try:
                self.window.controller.chat.common.lock_input()  # lock input
                current_mode = self.window.core.config.get('mode')

                # event: before mode select (inline mode can be select here)
                event = Event(Event.MODE_BEFORE, {
                    'value': mode,
                    'prompt': text,
                })
                event.ctx = ctx
                self.window.core.dispatcher.dispatch(event)
                mode = event.data['value']

                # Langchain mode
                if mode == "langchain":
                    self.log("Calling Langchain...")  # log
                    self.window.core.chain.system_prompt = sys_prompt
                    self.window.core.chain.user_name = ctx.input_name
                    self.window.core.chain.ai_name = ctx.output_name
                    result = self.window.core.chain.call(
                        text,
                        ctx,
                        stream_mode
                    )

                # Llama index mode
                elif mode == "llama_index":
                    self.log("Calling Llama-index...")  # log
                    idx = self.window.controller.idx.current_idx

                    # query index
                    if self.window.core.config.get('llama.idx.raw'):
                        result = self.window.core.idx.chat.raw_query(
                            ctx,
                            idx=idx,
                            model=model_data,
                            sys_prompt=sys_prompt,
                            stream=stream_mode
                        )

                    # chat or query index (if chat is not enabled)
                    else:
                        result = self.window.core.idx.chat.call(
                            ctx,
                            idx=idx,
                            model=model_data,
                            sys_prompt=sys_prompt,
                            stream=stream_mode
                        )

                # OpenAI API mode(s)
                else:
                    self.log("Calling OpenAI API...")  # log
                    self.window.core.gpt.system_prompt = sys_prompt
                    self.window.core.gpt.user_name = ctx.input_name
                    self.window.core.gpt.ai_name = ctx.output_name
                    self.window.core.gpt.assistant_id = self.window.core.config.get('assistant')
                    self.window.core.gpt.thread_id = ctx.thread
                    self.window.core.gpt.attachments = self.window.core.attachments.get_all(current_mode)
                    result = self.window.core.gpt.call(
                        text,
                        mode,
                        ctx,
                        stream_mode
                    )

                # update context in DB
                ctx.current = False  # reset current state
                self.window.core.ctx.update_item(ctx)

                # launch assistants listener in background
                if mode == 'assistant':
                    self.window.core.ctx.append_run(ctx.run_id)  # get run ID and save it in ctx
                    self.window.controller.assistant.threads.handle_run(ctx)  # handle assistant run

                if result:
                    self.log("Context: output: {}".format(self.window.core.ctx.dump(ctx)))  # log
                else:
                    self.log("Context: output: None")
                    self.window.ui.dialogs.alert(trans('status.error'))
                    self.window.ui.status(trans('status.error'))

            except Exception as e:
                self.log("GPT output error: {}".format(e))  # log
                self.window.core.debug.log(e)
                self.window.ui.dialogs.alert(str(e))
                self.window.ui.status(trans('status.error'))
                print("Error when calling API: " + str(e))

            # handle response (if no assistant mode)
            # assistant response is handled in assistant thread
            if mode != "assistant":
                self.window.controller.chat.output.handle(ctx, mode, stream_mode)

        except Exception as e:
            self.log("Output error: {}".format(e))  # log
            self.window.core.debug.log(e)
            self.window.ui.dialogs.alert(str(e))
            self.window.ui.status(trans('status.error'))
            print("Error in sending text: " + str(e))

        # if commands enabled: post-execute commands (if no assistant mode)
        if mode != "assistant":
            self.window.controller.chat.output.handle_cmd(ctx)
            self.window.core.ctx.update_item(ctx)  # update ctx in DB

        # render: end
        self.window.controller.chat.render.end(stream=stream_mode)

        self.window.controller.chat.common.unlock_input()  # unlock

        # handle ctx name (generate title from summary if not initialized)
        if self.window.core.config.get('ctx.auto_summary'):
            self.window.controller.ctx.prepare_name(ctx)  # async

        return ctx

    def log(self, data: any):
        """
        Log data to debug

        :param data: Data to log
        """
        self.window.controller.debug.log(data, True)
