#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ================================================== #
# This file is a part of PYGPT package               #
# Website: https://pygpt.net                         #
# GitHub:  https://github.com/szczyglis-dev/py-gpt   #
# MIT License                                        #
# Created By  : Marcin Szczygliński                  #
# Updated Date: 2024.01.25 19:00:00                  #
# ================================================== #

import json

from pygpt_net.item.ctx import CtxItem


class Event:

    # Events
    AI_NAME = "ai.name"
    AUDIO_INPUT_STOP = "audio.input.stop"
    AUDIO_INPUT_TOGGLE = "audio.input.toggle"
    AUDIO_OUTPUT_STOP = "audio.output.stop"
    AUDIO_OUTPUT_TOGGLE = "audio.output.toggle"
    AUDIO_READ_TEXT = "audio.read_text"
    CMD_EXECUTE = "cmd.execute"
    CMD_INLINE = "cmd.inline"
    CMD_SYNTAX = "cmd.syntax"
    CTX_AFTER = "ctx.after"
    CTX_BEFORE = "ctx.before"
    CTX_BEGIN = "ctx.begin"
    CTX_END = "ctx.end"
    CTX_SELECT = "ctx.select"
    DISABLE = "disable"
    ENABLE = "enable"
    FORCE_STOP = "force.stop"
    INPUT_BEFORE = "input.before"
    MODE_BEFORE = "mode.before"
    MODE_SELECT = "mode.select"
    MODEL_BEFORE = "model.before"
    MODEL_SELECT = "model.select"
    PLUGIN_SETTINGS_CHANGED = "plugin.settings.changed"
    PLUGIN_OPTION_GET = "plugin.option.get"
    POST_PROMPT = "post.prompt"
    PRE_PROMPT = "pre.prompt"
    SYSTEM_PROMPT = "system.prompt"
    UI_ATTACHMENTS = "ui.attachments"
    UI_VISION = "ui.vision"
    USER_NAME = "user.name"
    USER_SEND = "user.send"

    def __init__(
            self,
            name: str = None,
            data: dict = None,
            ctx: CtxItem = None
    ):
        """
        Event object class

        :param name: event name
        :param data: event data
        :param ctx: context instance
        """
        self.name = name
        self.data = data
        self.ctx = ctx  # CtxItem
        self.stop = False  # True to stop propagation
        self.internal = False
        # internal event, not called from user
        # internal event is handled synchronously, ctx item has internal flag


class Dispatcher:
    def __init__(self, window=None):
        """
        Event dispatcher

        :param window: Window instance
        """
        self.window = window

    def dispatch(
            self,
            event: Event,
            all: bool = False
    ) -> (list, Event):
        """
        Dispatch event to plugins

        :param event: event to dispatch
        :param all: true if dispatch to all plugins (enabled or not)
        :return: list of affected plugins ids and event object
        """
        affected = []
        for id in self.window.core.plugins.plugins:
            if self.window.controller.plugins.is_enabled(id) or all:
                if event.stop:
                    break
                self.apply(id, event)
                affected.append(id)

        return affected, event

    def apply(
            self,
            id: str,
            event: Event
    ):
        """
        Handle event in plugin with provided id

        :param id: plugin id
        :param event: event object
        """
        if id in self.window.core.plugins.plugins:
            try:
                self.window.core.plugins.plugins[id].handle(event)
            except AttributeError:
                pass

    def reply(self, ctx: CtxItem):
        """
        Send reply from plugins to model

        :param ctx: context object
        """
        if ctx is not None:
            self.window.ui.status("")  # clear status
            if ctx.reply:
                self.window.core.ctx.update_item(ctx)  # update context in db
                self.window.ui.status('...')
                self.window.controller.chat.input.send(
                    json.dumps(ctx.results),
                    force=True,
                    reply=True,
                    internal=ctx.internal,
                )
