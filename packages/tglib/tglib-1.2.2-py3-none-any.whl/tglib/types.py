#!/bin/python3

__all__ = [
    'Animation',
    'Audio',
    'BotCommand',
    'BotCommandScope',
    'BotCommandScopeAllChatAdministrators',
    'BotCommandScopeAllGroupChats',
    'BotCommandScopeAllPrivateChats',
    'BotCommandScopeChat',
    'BotCommandScopeChatAdministrators',
    'BotCommandScopeChatMember',
    'BotCommandScopeDefault',
    'BotDescription',
    'BotName',
    'BotShortDescription',
    'CallbackGame',
    'CallbackQuery',
    'Chat',
    'ChatAdministratorRights',
    'ChatBoost',
    'ChatBoostSource',
    'ChatBoostSourcePremium',
    'ChatBoostSourceGiftCode',
    'ChatBoostSourceGiveaway',
    'ChatBoostUpdated',
    'ChatBoostRemoved',
    'ChatInviteLink',
    'ChatJoinRequest',
    'ChatLocation',
    'ChatMember',
    'ChatMemberAdministrator',
    'ChatMemberBanned',
    'ChatMemberLeft',
    'ChatMemberMember',
    'ChatMemberOwner',
    'ChatMemberRestricted',
    'ChatMemberUpdated',
    'ChatPermissions',
    'ChatPhoto',
    'ChatShared',
    'ChosenInlineResult',
    'Contact',
    'Dice',
    'Document',
    'EncryptedCredentials',
    'EncryptedPassportElement',
    'ExternalReplyInfo',
    'File',
    'ForceReply',
    'ForumTopic',
    'ForumTopicClosed',
    'ForumTopicCreated',
    'ForumTopicEdited',
    'ForumTopicReopened',
    'Game',
    'GameHighScore',
    'GeneralForumTopicHidden',
    'GeneralForumTopicUnhidden',
    'Giveaway',
    'GiveawayCompleted',
    'GiveawayCreated',
    'GiveawayWinners',
    'InaccessibleMessage',
    'InlineKeyboardButton',
    'InlineKeyboardMarkup',
    'InlineQuery',
    'InlineQueryResult',
    'InlineQueryResultArticle',
    'InlineQueryResultAudio',
    'InlineQueryResultCachedAudio',
    'InlineQueryResultCachedDocument',
    'InlineQueryResultCachedGif',
    'InlineQueryResultCachedMpeg4Gif',
    'InlineQueryResultCachedPhoto',
    'InlineQueryResultCachedSticker',
    'InlineQueryResultCachedVideo',
    'InlineQueryResultCachedVoice',
    'InlineQueryResultContact',
    'InlineQueryResultDocument',
    'InlineQueryResultGame',
    'InlineQueryResultGif',
    'InlineQueryResultLocation',
    'InlineQueryResultMpeg4Gif',
    'InlineQueryResultPhoto',
    'InlineQueryResultVenue',
    'InlineQueryResultVideo',
    'InlineQueryResultVoice',
    'InlineQueryResultsButton',
    'InputContactMessageContent',
    'InputFile',
    'InputInvoiceMessageContent',
    'InputLocationMessageContent',
    'InputMedia',
    'InputMediaAnimation',
    'InputMediaAudio',
    'InputMediaDocument',
    'InputMediaPhoto',
    'InputMediaVideo',
    'InputMessageContent',
    'InputSticker',
    'InputTextMessageContent',
    'InputVenueMessageContent',
    'Invoice',
    'KeyboardButton',
    'KeyboardButtonPollType',
    'KeyboardButtonRequestChat',
    'KeyboardButtonRequestUsers',
    'LabeledPrice',
    'LinkPreviewOptions',
    'Location',
    'LoginUrl',
    'MaskPosition',
    'MaybeInaccessibleMessage',
    'MenuButton',
    'MenuButtonCommands',
    'MenuButtonDefault',
    'MenuButtonWebApp',
    'Message',
    'MessageAutoDeleteTimerChanged',
    'MessageEntity',
    'MessageId',
    'MessageOrigin',
    'MessageOriginUser',
    'MessageOriginHiddenUser',
    'MessageOriginChat',
    'MessageOriginChannel',
    'MessageReactionCountUpdated',
    'MessageReactionUpdated',
    'OrderInfo',
    'PassportData',
    'PassportElementError',
    'PassportElementErrorDataField',
    'PassportElementErrorFile',
    'PassportElementErrorFiles',
    'PassportElementErrorFrontSide',
    'PassportElementErrorReverseSide',
    'PassportElementErrorSelfie',
    'PassportElementErrorTranslationFile',
    'PassportElementErrorTranslationFiles',
    'PassportElementErrorUnspecified',
    'PassportFile',
    'PhotoSize',
    'Poll',
    'PollAnswer',
    'PollOption',
    'PreCheckoutQuery',
    'ProximityAlertTriggered',
    'ReactionCount',
    'ReactionType',
    'ReactionTypeEmoji',
    'ReactionTypeCustomEmoji',
    'ReplyKeyboardMarkup',
    'ReplyKeyboardRemove',
    'ReplyParameters',
    'ResponseParameters',
    'SentWebAppMessage',
    'ShippingAddress',
    'ShippingOption',
    'ShippingQuery',
    'Sticker',
    'StickerSet',
    'Story',
    'SuccessfulPayment',
    'SwitchInlineQueryChosenChat',
    'TextQuote',
    'Update',
    'User',
    'UserChatBoosts',
    'UserProfilePhotos',
    'UsersShared',
    'Venue',
    'Video',
    'VideoChatEnded',
    'VideoChatParticipantsInvited',
    'VideoChatScheduled',
    'VideoChatStarted',
    'VideoNote',
    'Voice',
    'WebAppData',
    'WebAppInfo',
    'WriteAccessAllowed'
]

import os
from typing import (Any,
                    Union,
                    Literal,
                    Optional)

from .logger import get_logger
logger = get_logger('TelegramTypes')

try:
    import ujson as json
except ImportError:
    import json
    logger.info(
        "module 'ujson' not found, the"
        " default 'json' was imported."
    )


def _check_dict(result: dict) -> dict:

    if not isinstance(result, dict):
        raise TypeError(
            'Expected dict as parameter in'
            f' _check_dict(), got {result.__class__}'
        )
    if 'from' in result:
        result['from_user'] = result['from']
        del result['from']

    return result


class TelegramType:
    ...


def _serialize(
    val: Any,
    *,
    last: bool = True
) -> Union[Any, str, list, dict]:

    if isinstance(val, TelegramType):
        val = val.__dict__

    elif hasattr(val, '__dict__'):
        val = '{!r}'.format(val)

    if isinstance(val, (list, tuple)):
        res = []
        for x in val:
            res.append(
                _serialize(x, last = False)
            )

    elif isinstance(val, dict):
        res = {}
        for x, y in val.items():
            if y is not None:
                res.update(
                    {x: _serialize(y, last = False)}
                )
    else:
        res = val

    if not last:
        return res
    else:
        return res if isinstance(res, str) else json.dumps(res, ensure_ascii = False)


def _get_kwargs(obj: TelegramType, kwargs: dict) -> bool:
    if kwargs:
        logger.debug(
            f'Got {len(kwargs)} unexpected arguments'
            f' in {obj.__class__.__name__}: {kwargs}'
        )
        return True
    return False


class ChatPermissions(TelegramType):
    '''
    https://core.telegram.org/bots/api#chatpermissions
    Describes actions that a non-administrator user is allowed to take in a chat.
    '''
    @classmethod
    def dese(cls, result):
        if result is None: return None
        obj = _check_dict(result)
        obj['can_send_messages'] = obj.get('can_send_messages')
        obj['can_send_audios'] = obj.get('can_send_audios')
        obj['can_send_documents'] = obj.get('can_send_documents')
        obj['can_send_photos'] = obj.get('can_send_photos')
        obj['can_send_videos'] = obj.get('can_send_videos')
        obj['can_send_video_notes'] = obj.get('can_send_video_notes')
        obj['can_send_voice_notes'] = obj.get('can_send_voice_notes')
        obj['can_send_polls'] = obj.get('can_send_polls')
        obj['can_send_other_messages'] = obj.get('can_send_other_messages')
        obj['can_add_web_page_previews'] = obj.get('can_add_web_page_previews')
        obj['can_change_info'] = obj.get('can_change_info')
        obj['can_invite_users'] = obj.get('can_invite_users')
        obj['can_pin_messages'] = obj.get('can_pin_messages')
        obj['can_manage_topics'] = obj.get('can_manage_topics')
        return cls(**obj)

    def __init__(
        self,
        can_send_messages: Optional[bool] = None,
        can_send_audios: Optional[bool] = None,
        can_send_documents: Optional[bool] = None,
        can_send_photos: Optional[bool] = None,
        can_send_videos: Optional[bool] = None,
        can_send_video_notes: Optional[bool] = None,
        can_send_voice_notes: Optional[bool] = None,
        can_send_polls: Optional[bool] = None,
        can_send_other_messages: Optional[bool] = None,
        can_add_web_page_previews: Optional[bool] = None,
        can_change_info: Optional[bool] = None,
        can_invite_users: Optional[bool] = None,
        can_pin_messages: Optional[bool] = None,
        can_manage_topics: Optional[bool] = None,
        **kwargs
    ):
        _get_kwargs(self, kwargs)
        self.can_send_messages = can_send_messages
        self.can_send_audios = can_send_audios
        self.can_send_documents = can_send_documents
        self.can_send_photos = can_send_photos
        self.can_send_videos = can_send_videos
        self.can_send_video_notes = can_send_video_notes
        self.can_send_voice_notes = can_send_voice_notes
        self.can_send_polls = can_send_polls
        self.can_send_other_messages = can_send_other_messages
        self.can_add_web_page_previews = can_add_web_page_previews
        self.can_change_info = can_change_info
        self.can_invite_users = can_invite_users
        self.can_pin_messages = can_pin_messages
        self.can_manage_topics = can_manage_topics


class ChatAdministratorRights(TelegramType):
    '''
    https://core.telegram.org/bots/api#chatadministratorrights
    Represents the rights of an administrator in a chat.
    '''
    @classmethod
    def dese(cls, result):
        if result is None: return None
        obj = _check_dict(result)
        obj['is_anonymous'] = obj.get('is_anonymous')
        obj['can_manage_chat'] = obj.get('can_manage_chat')
        obj['can_delete_messages'] = obj.get('can_delete_messages')
        obj['can_manage_video_chats'] = obj.get('can_manage_video_chats')
        obj['can_restrict_members'] = obj.get('can_restrict_members')
        obj['can_promote_members'] = obj.get('can_promote_members')
        obj['can_change_info'] = obj.get('can_change_info')
        obj['can_invite_users'] = obj.get('can_invite_users')
        obj['can_post_messages'] = obj.get('can_post_messages')
        obj['can_edit_messages'] = obj.get('can_edit_messages')
        obj['can_pin_messages'] = obj.get('can_pin_messages')
        obj['can_post_stories'] = obj.get('can_post_stories')
        obj['can_edit_stories'] = obj.get('can_edit_stories')
        obj['can_delete_stories'] = obj.get('can_delete_stories')
        obj['can_manage_topics'] = obj.get('can_manage_topics')
        return cls(**obj)

    def __init__(
        self,
        is_anonymous: bool,
        can_manage_chat: bool,
        can_delete_messages: bool,
        can_manage_video_chats: bool,
        can_restrict_members: bool,
        can_promote_members: bool,
        can_change_info: bool,
        can_invite_users: bool,
        can_post_messages: Optional[bool] = None,
        can_edit_messages: Optional[bool] = None,
        can_pin_messages: Optional[bool] = None,
        can_post_stories: Optional[bool] = None,
        can_edit_stories: Optional[bool] = None,
        can_delete_stories: Optional[bool] = None,
        can_manage_topics: Optional[bool] = None,
        **kwargs
    ):
        _get_kwargs(self, kwargs)
        self.is_anonymous = is_anonymous
        self.can_manage_chat = can_manage_chat
        self.can_delete_messages = can_delete_messages
        self.can_manage_video_chats = can_manage_video_chats
        self.can_restrict_members = can_restrict_members
        self.can_promote_members = can_promote_members
        self.can_change_info = can_change_info
        self.can_invite_users = can_invite_users
        self.can_post_messages = can_post_messages
        self.can_edit_messages = can_edit_messages
        self.can_pin_messages = can_pin_messages
        self.can_post_stories = can_post_stories
        self.can_edit_stories = can_edit_stories
        self.can_delete_stories = can_delete_stories
        self.can_manage_topics = can_manage_topics


class SwitchInlineQueryChosenChat(TelegramType):
    '''
    https://core.telegram.org/bots/api#switchinlinequerychosenchat
    This object represents an inline button that switches the current user
    to inline mode in a chosen chat, with an optional default inline query.
    '''
    @classmethod
    def dese(cls, result):
        if result is None: return None
        obj = _check_dict(result)
        obj['query'] = obj.get('query')
        obj['allow_user_chats'] = obj.get('allow_user_chats')
        obj['allow_bot_chats'] = obj.get('allow_bot_chats')
        obj['allow_group_chats'] = obj.get('allow_group_chats')
        obj['allow_channel_chats'] = obj.get('allow_channel_chats')
        return cls(**obj)

    def __init__(
        self,
        query: Optional[str] = None,
        allow_user_chats: Optional[bool] = None,
        allow_bot_chats: Optional[bool] = None,
        allow_group_chats: Optional[bool] = None,
        allow_channel_chats: Optional[bool] = None
    ):
        self.query = query
        self.allow_user_chats = allow_user_chats
        self.allow_bot_chats = allow_bot_chats
        self.allow_group_chats = allow_group_chats
        self.allow_channel_chats = allow_channel_chats


class CallbackGame(TelegramType):
    '''
    https://core.telegram.org/bots/api#callbackgame
    A placeholder, currently holds no information. Use BotFather to set up your game.
    '''
    @classmethod
    def dese(cls, result):
        if result is None: return None
        obj = _check_dict(result)
        return cls(**obj)

    def __init__(
        self,
        **kwargs
    ):
        _get_kwargs(self, kwargs)
        self.__dict__ = kwargs


class InputFile(TelegramType):
    '''
    https://core.telegram.org/bots/api#inputfile
    This object represents the contents of a file to be uploaded. Must be posted
    using multipart/form-data in the usual way that files are uploaded via the browser.
    '''
    def __init__(
        self,
        path: str,
        file_name: Optional[str] = None,
        hide_name: Optional[bool] = False
    ):
        self.path = path
        if not file_name and not hide_name:
            self.file_name = os.path.basename(path)
        elif file_name and not hide_name:
            self.file_name = file_name
        else:
            self.file_name = None


class LoginUrl(TelegramType):
    '''
    https://core.telegram.org/bots/api#loginurl
    This object represents a parameter of the inline keyboard button used to automatically authorize
    a user. Serves as a great replacement for the Telegram Login Widget when the user is coming from
    Telegram. All the user needs to do is tap/click a button and confirm that they want to log in.
    '''
    @classmethod
    def dese(cls, result):
        if result is None: return None
        obj = _check_dict(result)
        obj['url'] = obj.get('url')
        obj['forward_text'] = obj.get('forward_text')
        obj['bot_username'] = obj.get('bot_username')
        obj['request_write_access'] = obj.get('request_write_access')
        return cls(**obj)

    def __init__(
        self,
        url: str,
        forward_text: Optional[str] = None,
        bot_username: Optional[str] = None,
        request_write_access: Optional[bool] = None
    ):
        self.url = url
        self.forward_text = forward_text
        self.bot_username = bot_username
        self.request_write_access = request_write_access


class LabeledPrice(TelegramType):
    '''
    https://core.telegram.org/bots/api#labeledprice
    This object represents a portion of the price for goods or services.
    '''
    def __init__(
        self,
        label: str,
        amount: int
    ):
        self.label = label
        self.amount = amount


class LinkPreviewOptions(TelegramType):
    '''
    https://core.telegram.org/bots/api#linkpreviewoptions
    Describes the options used for link preview generation.
    '''
    @classmethod
    def dese(cls, result):
        if result is None: return None
        obj = _check_dict(result)
        obj['is_disabled'] = obj.get('is_disabled')
        obj['url'] = obj.get('url')
        obj['prefer_small_media'] = obj.get('prefer_small_media')
        obj['prefer_large_media'] = obj.get('prefer_large_media')
        obj['show_above_text'] = obj.get('show_above_text')
        return cls(**obj)

    def __init__(
        self,
        is_disabled: Optional[bool] = None,
        url: Optional[str] = None,
        prefer_small_media: Optional[bool] = None,
        prefer_large_media: Optional[bool] = None,
        show_above_text: Optional[bool] = None
    ):
        self.is_disabled = is_disabled
        self.url = url
        self.prefer_small_media = prefer_small_media
        self.prefer_large_media = prefer_large_media
        self.show_above_text = show_above_text


class User(TelegramType):
    '''
    https://core.telegram.org/bots/api#user
    This object represents a Telegram user or bot.
    '''
    @classmethod
    def dese(cls, result):
        if result is None: return None
        obj = _check_dict(result)
        obj['id'] = obj.get('id')
        obj['is_bot'] = obj.get('is_bot')
        obj['first_name'] = obj.get('first_name')
        obj['last_name'] = obj.get('last_name')
        obj['username'] = obj.get('username')
        obj['language_code'] = obj.get('language_code')
        obj['is_premium'] = obj.get('is_premium')
        obj['added_to_attachment_menu'] = obj.get('added_to_attachment_menu')
        obj['can_join_groups'] = obj.get('can_join_groups')
        obj['can_read_all_group_messages'] = obj.get('can_read_all_group_messages')
        obj['supports_inline_queries'] = obj.get('supports_inline_queries')
        return cls(**obj)

    def __init__(
        self,
        id: int,
        is_bot: bool,
        first_name: str,
        last_name: Optional[str] = None,
        username: Optional[str] = None,
        language_code: Optional[str] = None,
        is_premium: Optional[Literal[True]] = None,
        added_to_attachment_menu: Optional[Literal[True]] = None,
        can_join_groups: Optional[bool] = None,
        can_read_all_group_messages: Optional[bool] = None,
        supports_inline_queries: Optional[bool] = None,
        **kwargs
    ):
        _get_kwargs(self, kwargs)
        self.id = id
        self.is_bot = is_bot
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.language_code = language_code
        self.is_premium = is_premium
        self.added_to_attachment_menu = added_to_attachment_menu
        self.can_join_groups = can_join_groups
        self.can_read_all_group_messages = can_read_all_group_messages
        self.supports_inline_queries = supports_inline_queries


class MessageEntity(TelegramType):
    '''
    https://core.telegram.org/bots/api#messageentity
    This object represents one special entity in a text message. For example, hashtags, usernames, URLs, etc.
    '''
    @classmethod
    def dese(cls, result):
        if result is None: return None
        obj = _check_dict(result)
        obj['type'] = obj.get('type')
        obj['offset'] = obj.get('offset')
        obj['length'] = obj.get('length')
        obj['url'] = obj.get('url')
        obj['user'] = User.dese(obj.get('user'))
        obj['language'] = obj.get('language')
        obj['custom_emoji_id'] = obj.get('custom_emoji_id')
        return cls(**obj)

    def __init__(
        self,
        type: str,
        offset: int,
        length: int,
        url: Optional[str] = None,
        user: Optional[User] = None,
        language: Optional[str] = None,
        custom_emoji_id: Optional[str] = None
    ):
        self.type = type
        self.offset = offset
        self.length = length
        self.url = url
        self.user = user
        self.language = language
        self.custom_emoji_id = custom_emoji_id


class TextQuote(TelegramType):
    '''
    https://core.telegram.org/bots/api#textquote
    This object contains information about the quoted part of a message that is replied to by the given message.
    '''
    @classmethod
    def dese(cls, result):
        if result is None: return None
        obj = _check_dict(result)
        obj['text'] = obj.get('text')
        obj['position'] = obj.get('position')
        obj['entities'] = [MessageEntity.dese(kwargs) for kwargs in obj.get('entities')] if 'entities' in obj else None
        obj['is_manual'] = obj.get('is_manual')
        return cls(**obj)

    def __init__(
        self,
        text: str,
        position: int,
        entities: Optional[list[MessageEntity]] = None,
        is_manual: Optional[Literal[True]] = None,
        **kwargs
    ):
        _get_kwargs(self, kwargs)
        self.text = text
        self.position = position
        self.entities = entities
        self.is_manual = is_manual


class ReplyParameters(TelegramType):
    '''
    https://core.telegram.org/bots/api#replyparameters
    Describes reply parameters for the message that is being sent.
    '''
    def __init__(
        self,
        message_id: int,
        chat_id: Optional[Union[int, str]] = None,
        allow_sending_without_reply: Optional[bool] = None,
        quote: Optional[str] = None,
        quote_parse_mode: Optional[str] = None,
        quote_entities: Optional[list[MessageEntity]] = None,
        quote_position: Optional[int] = None
    ):
        self.message_id = message_id
        self.chat_id = chat_id
        self.allow_sending_without_reply = allow_sending_without_reply
        self.quote = quote
        self.quote_parse_mode = quote_parse_mode
        self.quote_entities = quote_entities
        self.quote_position = quote_position


# MaybeInaccessibleMessage: 2 SUBCLASSES

class MaybeInaccessibleMessage(TelegramType):
    '''
    https://core.telegram.org/bots/api#maybeinaccessiblemessage
    This object describes a message that can be inaccessible to the bot. It can be one of:
    - Message
    - InaccessibleMessage
    '''
    @classmethod
    def dese(cls, result):
        if result is None: return None
        obj = _check_dict(result)
        date = obj['date']

        obj['chat'] = Chat.dese(obj.get('chat'))

        if date == 0:
            return InaccessibleMessage(**obj)
        else:
            return Message(**obj)


class InaccessibleMessage(MaybeInaccessibleMessage):
    '''
    https://core.telegram.org/bots/api#inaccessiblemessage
    This object describes a message that was deleted or is otherwise inaccessible to the bot.
    '''
    def __init__(
        self,
        chat,
        message_id,
        date = 0,
        **kwargs
    ):
        _get_kwargs(self, kwargs)
        self.chat: Chat = chat
        self.message_id: int = message_id
        self.date: int = date


class Message(MaybeInaccessibleMessage):
    '''
    https://core.telegram.org/bots/api#message
    This object represents a message.
    '''
    @classmethod
    def dese(cls, result):
        if result is None: return None
        obj = _check_dict(result)
        obj['message_id'] = obj.get('message_id')
        obj['date'] = obj.get('date')
        obj['chat'] = Chat.dese(obj.get('chat'))
        obj['message_thread_id'] = obj.get('message_thread_id')
        obj['from_user'] = User.dese(obj.get('from_user'))
        obj['sender_chat'] = Chat.dese(obj.get('sender_chat'))
        obj['forward_origin'] = MessageOrigin.dese(obj.get('forward_origin'))
        obj['is_topic_message'] = obj.get('is_topic_message')
        obj['is_automatic_forward'] = obj.get('is_automatic_forward')
        obj['reply_to_message'] = Message.dese(obj.get('reply_to_message'))
        obj['external_reply'] = ExternalReplyInfo.dese(obj.get('external_reply'))
        obj['quote'] = TextQuote.dese(obj.get('quote'))
        obj['via_bot'] = User.dese(obj.get('via_bot'))
        obj['edit_date'] = obj.get('edit_date')
        obj['has_protected_content'] = obj.get('has_protected_content')
        obj['media_group_id'] = obj.get('media_group_id')
        obj['author_signature'] = obj.get('author_signature')
        obj['text'] = obj.get('text')
        obj['entities'] = [MessageEntity.dese(kwargs) for kwargs in obj.get('entities')] if 'entities' in obj else None
        obj['link_preview_options'] = LinkPreviewOptions.dese(obj.get('link_preview_options'))
        obj['animation'] = Animation.dese(obj.get('animation'))
        obj['audio'] = Audio.dese(obj.get('audio'))
        obj['document'] = Document.dese(obj.get('document'))
        obj['photo'] = [PhotoSize.dese(kwargs) for kwargs in obj.get('photo')] if 'photo' in obj else None
        obj['sticker'] = Sticker.dese(obj.get('sticker'))
        obj['story'] = Story.dese(obj.get('story'))
        obj['video'] = Video.dese(obj.get('video'))
        obj['video_note'] = VideoNote.dese(obj.get('video_note'))
        obj['voice'] = Voice.dese(obj.get('voice'))
        obj['caption'] = obj.get('caption')
        obj['caption_entities'] = [MessageEntity.dese(kwargs) for kwargs in obj.get('caption_entities')] if 'caption_entities' in obj else None
        obj['has_media_spoiler'] = obj.get('has_media_spoiler')
        obj['contact'] = Contact.dese(obj.get('contact'))
        obj['dice'] = Dice.dese(obj.get('dice'))
        obj['game'] = Game.dese(obj.get('game'))
        obj['poll'] = Poll.dese(obj.get('poll'))
        obj['venue'] = Venue.dese(obj.get('venue'))
        obj['location'] = Location.dese(obj.get('location'))
        obj['new_chat_members'] = [User.dese(kwargs) for kwargs in obj.get('new_chat_members')] if 'new_chat_members' in obj else None
        obj['left_chat_member'] = User.dese(obj.get('left_chat_member'))
        obj['new_chat_title'] = obj.get('new_chat_title')
        obj['new_chat_photo'] = [PhotoSize.dese(kwargs) for kwargs in obj.get('new_chat_photo')] if 'new_chat_photo' in obj else None
        obj['delete_chat_photo'] = obj.get('delete_chat_photo')
        obj['group_chat_created'] = obj.get('group_chat_created')
        obj['supergroup_chat_created'] = obj.get('supergroup_chat_created')
        obj['channel_chat_created'] = obj.get('channel_chat_created')
        obj['message_auto_delete_timer_changed'] = MessageAutoDeleteTimerChanged.dese(obj.get('message_auto_delete_timer_changed'))
        obj['migrate_to_chat_id'] = obj.get('migrate_to_chat_id')
        obj['migrate_from_chat_id'] = obj.get('migrate_from_chat_id')
        obj['pinned_message'] = MaybeInaccessibleMessage.dese(obj.get('pinned_message'))
        obj['invoice'] = Invoice.dese(obj.get('invoice'))
        obj['successful_payment'] = SuccessfulPayment.dese(obj.get('successful_payment'))
        obj['users_shared'] = UsersShared.dese(obj.get('users_shared'))
        obj['chat_shared'] = ChatShared.dese(obj.get('chat_shared'))
        obj['connected_website'] = obj.get('connected_website')
        obj['write_access_allowed'] = WriteAccessAllowed.dese(obj.get('write_access_allowed'))
        obj['passport_data'] = PassportData.dese(obj.get('passport_data'))
        obj['proximity_alert_triggered'] = ProximityAlertTriggered.dese(obj.get('proximity_alert_triggered'))
        obj['forum_topic_created'] = ForumTopicCreated.dese(obj.get('forum_topic_created'))
        obj['forum_topic_edited'] = ForumTopicEdited.dese(obj.get('forum_topic_edited'))
        obj['forum_topic_closed'] = ForumTopicClosed.dese(obj.get('forum_topic_closed'))
        obj['forum_topic_reopened'] = ForumTopicReopened.dese(obj.get('forum_topic_reopened'))
        obj['general_forum_topic_hidden'] = GeneralForumTopicHidden.dese(obj.get('general_forum_topic_hidden'))
        obj['general_forum_topic_unhidden'] = GeneralForumTopicUnhidden.dese(obj.get('general_forum_topic_unhidden'))
        obj['giveaway_created'] = GiveawayCreated.dese(obj.get('giveaway_created'))
        obj['giveaway'] = Giveaway.dese(obj.get('giveaway'))
        obj['giveaway_winners'] = GiveawayWinners.dese(obj.get('giveaway_winners'))
        obj['giveaway_completed'] = GiveawayCompleted.dese(obj.get('giveaway_completed'))
        obj['video_chat_scheduled'] = VideoChatScheduled.dese(obj.get('video_chat_scheduled'))
        obj['video_chat_started'] = VideoChatStarted.dese(obj.get('video_chat_started'))
        obj['video_chat_ended'] = VideoChatEnded.dese(obj.get('video_chat_ended'))
        obj['video_chat_participants_invited'] = VideoChatParticipantsInvited.dese(obj.get('video_chat_participants_invited'))
        obj['web_app_data'] = WebAppData.dese(obj.get('web_app_data'))
        obj['reply_markup'] = InlineKeyboardMarkup.dese(obj.get('reply_markup'))
        return cls(**obj)

    def __init__(
        self,
        message_id,
        date,
        chat,
        message_thread_id = None,
        from_user = None,
        sender_chat = None,
        forward_origin = None,
        is_topic_message = None,
        is_automatic_forward = None,
        reply_to_message = None,
        external_reply = None,
        quote = None,
        via_bot = None,
        edit_date = None,
        has_protected_content = None,
        media_group_id = None,
        author_signature = None,
        text = None,
        entities = None,
        link_preview_options = None,
        animation = None,
        audio = None,
        document = None,
        photo = None,
        sticker = None,
        story = None,
        video = None,
        video_note = None,
        voice = None,
        caption = None,
        caption_entities = None,
        has_media_spoiler = None,
        contact = None,
        dice = None,
        game = None,
        poll = None,
        venue = None,
        location = None,
        new_chat_members = None,
        left_chat_member = None,
        new_chat_title = None,
        new_chat_photo = None,
        delete_chat_photo = None,
        group_chat_created = None,
        supergroup_chat_created = None,
        channel_chat_created = None,
        message_auto_delete_timer_changed = None,
        migrate_to_chat_id = None,
        migrate_from_chat_id = None,
        pinned_message = None,
        invoice = None,
        successful_payment = None,
        users_shared = None,
        chat_shared = None,
        connected_website = None,
        write_access_allowed = None,
        passport_data = None,
        proximity_alert_triggered = None,
        forum_topic_created = None,
        forum_topic_edited = None,
        forum_topic_closed = None,
        forum_topic_reopened = None,
        general_forum_topic_hidden = None,
        general_forum_topic_unhidden = None,
        giveaway_created = None,
        giveaway = None,
        giveaway_winners = None,
        giveaway_completed = None,
        video_chat_scheduled = None,
        video_chat_started = None,
        video_chat_ended = None,
        video_chat_participants_invited = None,
        web_app_data = None,
        reply_markup = None,
        **kwargs
    ):
        _get_kwargs(self, kwargs)
        self.message_id: int = message_id
        self.date: int = date
        self.chat: Chat = chat
        self.message_thread_id: Optional[int] = message_thread_id
        self.from_user: Optional[User] = from_user
        self.sender_chat: Optional[Chat] = sender_chat
        self.forward_origin: Optional[MessageOrigin] = forward_origin
        self.is_topic_message: Optional[Literal[True]] = is_topic_message
        self.is_automatic_forward: Optional[Literal[True]] = is_automatic_forward
        self.reply_to_message: Optional[Message] = reply_to_message
        self.external_reply: Optional[ExternalReplyInfo] = external_reply
        self.quote: Optional[TextQuote] = quote
        self.via_bot: Optional[User] = via_bot
        self.edit_date: Optional[int] = edit_date
        self.has_protected_content: Optional[Literal[True]] = has_protected_content
        self.media_group_id: Optional[str] = media_group_id
        self.author_signature: Optional[str] = author_signature
        self.text: str = text if text is not None else str() # If not text, it's str() instead of None
        self.entities: Optional[list[MessageEntity]] = entities
        self.link_preview_options: Optional[LinkPreviewOptions] = link_preview_options
        self.animation: Optional[Animation] = animation
        self.audio: Optional[Audio] = audio
        self.document: Optional[Document] = document
        self.photo: Optional[list[PhotoSize]] = photo
        self.sticker: Optional[Sticker] = sticker
        self.story: Optional[Story] = story
        self.video: Optional[Video] = video
        self.video_note: Optional[VideoNote] = video_note
        self.voice: Optional[Voice] = voice
        self.caption: Optional[str] = caption
        self.caption_entities: Optional[list[MessageEntity]] = caption_entities
        self.has_media_spoiler: Optional[Literal[True]] = has_media_spoiler
        self.contact: Optional[Contact] = contact
        self.dice: Optional[Dice] = dice
        self.game: Optional[Game] = game
        self.poll: Optional[Poll] = poll
        self.venue: Optional[Venue] = venue
        self.location: Optional[Location] = location
        self.new_chat_members: Optional[list[User]] = new_chat_members
        self.left_chat_member: Optional[User] = left_chat_member
        self.new_chat_title: Optional[str] = new_chat_title
        self.new_chat_photo: Optional[list[PhotoSize]] = new_chat_photo
        self.delete_chat_photo: Optional[Literal[True]] = delete_chat_photo
        self.group_chat_created: Optional[Literal[True]] = group_chat_created
        self.supergroup_chat_created: Optional[Literal[True]] = supergroup_chat_created
        self.channel_chat_created: Optional[Literal[True]] = channel_chat_created
        self.message_auto_delete_timer_changed: Optional[MessageAutoDeleteTimerChanged] = message_auto_delete_timer_changed
        self.migrate_to_chat_id: Optional[int] = migrate_to_chat_id
        self.migrate_from_chat_id: Optional[int] = migrate_from_chat_id
        self.pinned_message: Optional[MaybeInaccessibleMessage] = pinned_message
        self.invoice: Optional[Invoice] = invoice
        self.successful_payment: Optional[SuccessfulPayment] = successful_payment
        self.users_shared: Optional[UsersShared] = users_shared
        self.chat_shared: Optional[ChatShared] = chat_shared
        self.connected_website: Optional[str] = connected_website
        self.write_access_allowed: Optional[WriteAccessAllowed] = write_access_allowed
        self.passport_data: Optional[PassportData] = passport_data
        self.proximity_alert_triggered: Optional[ProximityAlertTriggered] = proximity_alert_triggered
        self.forum_topic_created: Optional[ForumTopicCreated] = forum_topic_created
        self.forum_topic_edited: Optional[ForumTopicEdited] = forum_topic_edited
        self.forum_topic_closed: Optional[ForumTopicClosed] = forum_topic_closed
        self.forum_topic_reopened: Optional[ForumTopicReopened] = forum_topic_reopened
        self.general_forum_topic_hidden: Optional[GeneralForumTopicHidden] = general_forum_topic_hidden
        self.general_forum_topic_unhidden: Optional[GeneralForumTopicUnhidden] = general_forum_topic_unhidden
        self.giveaway_created: Optional[GiveawayCreated] = giveaway_created
        self.giveaway: Optional[Giveaway] = giveaway
        self.giveaway_winners: Optional[GiveawayWinners] = giveaway_winners
        self.giveaway_completed: Optional[GiveawayCompleted] = giveaway_completed
        self.video_chat_scheduled: Optional[VideoChatScheduled] = video_chat_scheduled
        self.video_chat_started: Optional[VideoChatStarted] = video_chat_started
        self.video_chat_ended: Optional[VideoChatEnded] = video_chat_ended
        self.video_chat_participants_invited: Optional[VideoChatParticipantsInvited] = video_chat_participants_invited
        self.web_app_data: Optional[WebAppData] = web_app_data
        self.reply_markup: Optional[InlineKeyboardMarkup] = reply_markup


class ChatPhoto(TelegramType):
    '''
    https://core.telegram.org/bots/api#chatphoto
    This object represents a chat photo.
    '''
    @classmethod
    def dese(cls, result):
        if result is None: return None
        obj = _check_dict(result)
        obj['small_file_id'] = obj.get('small_file_id')
        obj['small_file_unique_id'] = obj.get('small_file_unique_id')
        obj['big_file_id'] = obj.get('big_file_id')
        obj['big_file_unique_id'] = obj.get('big_file_unique_id')
        return cls(**obj)

    def __init__(
        self,
        small_file_id: str,
        small_file_unique_id: str,
        big_file_id: str,
        big_file_unique_id: str,
        **kwargs
    ):
        _get_kwargs(self, kwargs)
        self.small_file_id = small_file_id
        self.small_file_unique_id = small_file_unique_id
        self.big_file_id = big_file_id
        self.big_file_unique_id = big_file_unique_id


class Location(TelegramType):
    '''
    https://core.telegram.org/bots/api#location
    This object represents a point on the map.
    '''
    @classmethod
    def dese(cls, result):
        if result is None: return None
        obj = _check_dict(result)
        obj['longitude'] = obj.get('longitude')
        obj['latitude'] = obj.get('latitude')
        obj['horizontal_accuracy'] = obj.get('horizontal_accuracy')
        obj['live_period'] = obj.get('live_period')
        obj['heading'] = obj.get('heading')
        obj['proximity_alert_radius'] = obj.get('proximity_alert_radius')
        return cls(**obj)

    def __init__(
        self,
        longitude: float,
        latitude: float,
        horizontal_accuracy: Optional[float] = None,
        live_period: Optional[int] = None,
        heading: Optional[int] = None,
        proximity_alert_radius: Optional[int] = None,
        **kwargs
    ):
        _get_kwargs(self, kwargs)
        self.longitude = longitude
        self.latitude = latitude
        self.horizontal_accuracy = horizontal_accuracy
        self.live_period = live_period
        self.heading = heading
        self.proximity_alert_radius = proximity_alert_radius


class ChatLocation(TelegramType):
    '''
    https://core.telegram.org/bots/api#chatlocation
    Represents a location to which a chat is connected.
    '''
    @classmethod
    def dese(cls, result):
        if result is None: return None
        obj = _check_dict(result)
        obj['location'] = Location.dese(obj.get('location'))
        obj['address'] = obj.get('address')
        return cls(**obj)

    def __init__(
        self,
        location: Location,
        address: str,
        **kwargs
    ):
        _get_kwargs(self, kwargs)
        self.location = location
        self.address = address


# ReactionType: 2 SUBCLASSES

class ReactionType(TelegramType):
    '''
    https://core.telegram.org/bots/api#reactiontype
    This object describes the type of a reaction.
    Currently, it can be one of:
    - ReactionTypeEmoji
    - ReactionTypeCustomEmoji
    '''
    @classmethod
    def dese(cls, result):
        if result is None: return None
        obj = _check_dict(result)
        type = obj['type']

        if type == 'emoji':
            return ReactionTypeEmoji(**obj)

        elif type == 'custom_emoji':
            return ReactionTypeCustomEmoji(**obj)
        else:
            return cls(**obj)

    def __init__(
        self,
        **kwargs
    ):
        reaction_types = ', '.join([
            ReactionTypeEmoji.__name__,
            ReactionTypeCustomEmoji.__name__
        ])
        logger.warning(
            'ReactionType warning, expected one'
            f' of the following types: {reaction_types}.'
        )
        self.__dict__ = kwargs


class ReactionTypeEmoji(ReactionType):
    '''
    https://core.telegram.org/bots/api#reactiontypeemoji
    The reaction is based on an emoji.
    '''
    def __init__(
        self,
        emoji: str,
        type: str = 'emoji'
    ):
        self.type = type
        self.emoji = emoji


class ReactionTypeCustomEmoji(ReactionType):
    '''
    https://core.telegram.org/bots/api#reactiontypecustomemoji
    The reaction is based on a custom emoji.
    '''
    def __init__(
        self,
        custom_emoji_id: str,
        type: str = 'custom_emoji'
    ):
        self.type = type
        self.custom_emoji_id = custom_emoji_id


class Chat(TelegramType):
    '''
    https://core.telegram.org/bots/api#chat
    This object represents a chat.
    '''
    @classmethod
    def dese(cls, result):
        if result is None: return None
        obj = _check_dict(result)
        obj['id'] = obj.get('id')
        obj['type'] = obj.get('type')
        obj['title'] = obj.get('title')
        obj['username'] = obj.get('username')
        obj['first_name'] = obj.get('first_name')
        obj['last_name'] = obj.get('last_name')
        obj['is_forum'] = obj.get('is_forum')
        obj['photo'] = ChatPhoto.dese(obj.get('photo'))
        obj['active_usernames'] = obj.get('active_usernames')
        obj['available_reactions'] = [ReactionType.dese(kwargs) for kwargs in obj.get('available_reactions')] if 'available_reactions' in obj else None
        obj['accent_color_id'] = obj.get('accent_color_id')
        obj['background_custom_emoji_id'] = obj.get('background_custom_emoji_id')
        obj['profile_accent_color_id'] = obj.get('profile_accent_color_id')
        obj['profile_background_custom_emoji_id'] = obj.get('profile_background_custom_emoji_id')
        obj['emoji_status_custom_emoji_id'] = obj.get('emoji_status_custom_emoji_id')
        obj['emoji_status_expiration_date'] = obj.get('emoji_status_expiration_date')
        obj['bio'] = obj.get('bio')
        obj['has_private_forwards'] = obj.get('has_private_forwards')
        obj['has_restricted_voice_and_video_messages'] = obj.get('has_restricted_voice_and_video_messages')
        obj['join_to_send_messages'] = obj.get('join_to_send_messages')
        obj['join_by_request'] = obj.get('join_by_request')
        obj['description'] = obj.get('description')
        obj['invite_link'] = obj.get('invite_link')
        obj['pinned_message'] = Message.dese(obj.get('pinned_message'))
        obj['permissions'] = ChatPermissions.dese(obj.get('permissions'))
        obj['slow_mode_delay'] = obj.get('slow_mode_delay')
        obj['message_auto_delete_time'] = obj.get('message_auto_delete_time')
        obj['has_aggressive_anti_spam_enabled'] = obj.get('has_aggressive_anti_spam_enabled')
        obj['has_hidden_members'] = obj.get('has_hidden_members')
        obj['has_protected_content'] = obj.get('has_protected_content')
        obj['has_visible_history'] = obj.get('has_visible_history')
        obj['sticker_set_name'] = obj.get('sticker_set_name')
        obj['can_set_sticker_set'] = obj.get('can_set_sticker_set')
        obj['linked_chat_id'] = obj.get('linked_chat_id')
        obj['location'] = ChatLocation.dese(obj.get('location'))
        return cls(**obj)

    def __init__(
        self,
        id: int,
        type: str,
        title: Optional[str] = None,
        username: Optional[str] = None,
        first_name: Optional[str] = None,
        last_name: Optional[str] = None,
        is_forum: Optional[Literal[True]] = None,
        photo: Optional[ChatPhoto] = None,
        active_usernames: Optional[list[str]] = None,
        available_reactions: Optional[list[ReactionType]] = None,
        accent_color_id: Optional[int] = None,
        background_custom_emoji_id: Optional[str] = None,
        profile_accent_color_id: Optional[int] = None,
        profile_background_custom_emoji_id: Optional[str] = None,
        emoji_status_custom_emoji_id: Optional[str] = None,
        emoji_status_expiration_date: Optional[int] = None,
        bio: Optional[str] = None,
        has_private_forwards: Optional[Literal[True]] = None,
        has_restricted_voice_and_video_messages: Optional[Literal[True]] = None,
        join_to_send_messages: Optional[Literal[True]] = None,
        join_by_request: Optional[Literal[True]] = None,
        description: Optional[str] = None,
        invite_link: Optional[str] = None,
        pinned_message: Optional[Message] = None,
        permissions: Optional[ChatPermissions] = None,
        slow_mode_delay: Optional[int] = None,
        message_auto_delete_time: Optional[int] = None,
        has_aggressive_anti_spam_enabled: Optional[Literal[True]] = None,
        has_hidden_members: Optional[Literal[True]] = None,
        has_protected_content: Optional[Literal[True]] = None,
        has_visible_history: Optional[Literal[True]] = None,
        sticker_set_name: Optional[str] = None,
        can_set_sticker_set: Optional[Literal[True]] = None,
        linked_chat_id: Optional[int] = None,
        location: Optional[ChatLocation] = None,
        **kwargs
    ):
        _get_kwargs(self, kwargs)
        self.id = id
        self.type = type
        self.title = title
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.is_forum = is_forum
        self.photo = photo
        self.active_usernames = active_usernames
        self.available_reactions = available_reactions
        self.accent_color_id = accent_color_id
        self.background_custom_emoji_id = background_custom_emoji_id
        self.profile_accent_color_id = profile_accent_color_id
        self.profile_background_custom_emoji_id = profile_background_custom_emoji_id
        self.emoji_status_custom_emoji_id = emoji_status_custom_emoji_id
        self.emoji_status_expiration_date = emoji_status_expiration_date
        self.bio = bio
        self.has_private_forwards = has_private_forwards
        self.has_restricted_voice_and_video_messages = has_restricted_voice_and_video_messages
        self.join_to_send_messages = join_to_send_messages
        self.join_by_request = join_by_request
        self.description = description
        self.invite_link = invite_link
        self.pinned_message = pinned_message
        self.permissions = permissions
        self.slow_mode_delay = slow_mode_delay
        self.message_auto_delete_time = message_auto_delete_time
        self.has_aggressive_anti_spam_enabled = has_aggressive_anti_spam_enabled
        self.has_hidden_members = has_hidden_members
        self.has_protected_content = has_protected_content
        self.has_visible_history = has_visible_history
        self.sticker_set_name = sticker_set_name
        self.can_set_sticker_set = can_set_sticker_set
        self.linked_chat_id = linked_chat_id
        self.location = location


class MessageReactionUpdated(TelegramType):
    '''
    https://core.telegram.org/bots/api#messagereactionupdated
    This object represents a change of a reaction on a message performed by a user.
    '''
    @classmethod
    def dese(cls, result):
        if result is None: return None
        obj = _check_dict(result)
        obj['chat'] = Chat.dese(obj.get('chat'))
        obj['message_id'] = obj.get('message_id')
        obj['date'] = obj.get('date')
        obj['old_reaction'] = [ReactionType.dese(kwargs) for kwargs in obj.get('old_reaction')]
        obj['new_reaction'] = [ReactionType.dese(kwargs) for kwargs in obj.get('new_reaction')]
        obj['user'] = User.dese(obj.get('user'))
        obj['actor_chat'] = Chat.dese(obj.get('actor_chat'))
        return cls(**obj)

    def __init__(
        self,
        chat: Chat,
        message_id: int,
        date: int,
        old_reaction: list[ReactionType],
        new_reaction: list[ReactionType],
        user: Optional[User] = None,
        actor_chat: Optional[Chat] = None,
        **kwargs
    ):
        _get_kwargs(self, kwargs)
        self.chat = chat
        self.message_id = message_id
        self.date = date
        self.old_reaction = old_reaction
        self.new_reaction = new_reaction
        self.user = user
        self.actor_chat = actor_chat


class ReactionCount(TelegramType):
    '''
    https://core.telegram.org/bots/api#reactioncount
    Represents a reaction added to a message along with the number of times it was added.
    '''
    @classmethod
    def dese(cls, result):
        if result is None: return None
        obj = _check_dict(result)
        obj['type'] = ReactionType.dese(obj.get('type'))
        obj['total_count'] = obj.get('total_count')
        return cls(**obj)

    def __init__(
        self,
        type: ReactionType,
        total_count: int,
        **kwargs
    ):
        _get_kwargs(self, kwargs)
        self.type = type
        self.total_count = total_count


class MessageReactionCountUpdated(TelegramType):
    '''
    https://core.telegram.org/bots/api#messagereactioncountupdated
    This object represents reaction changes on a message with anonymous reactions.
    '''
    @classmethod
    def dese(cls, result):
        if result is None: return None
        obj = _check_dict(result)
        obj['chat'] = Chat.dese(obj.get('chat'))
        obj['message_id'] = obj.get('message_id')
        obj['date'] = obj.get('date')
        obj['reactions'] = [ReactionCount.dese(kwargs) for kwargs in obj.get('reactions')]
        return cls(**obj)

    def __init__(
        self,
        chat: Chat,
        message_id: int,
        date: int,
        reactions: list[ReactionCount],
        **kwargs
    ):
        _get_kwargs(self, kwargs)
        self.chat = chat
        self.message_id = message_id
        self.date = date
        self.reactions = reactions


class MessageId(TelegramType):
    '''
    https://core.telegram.org/bots/api#messageid
    This object represents a unique message identifier.
    '''
    @classmethod
    def dese(cls, result):
        if result is None: return None
        obj = _check_dict(result)
        obj['message_id'] = obj.get('message_id')
        return cls(**obj)

    def __init__(
        self,
        message_id: int,
        **kwargs
    ):
        _get_kwargs(self, kwargs)
        self.message_id = message_id


class PhotoSize(TelegramType):
    '''
    https://core.telegram.org/bots/api#photosize
    This object represents one size of a photo or a file / sticker thumbnail.
    '''
    @classmethod
    def dese(cls, result):
        if result is None: return None
        obj = _check_dict(result)
        obj['file_id'] = obj.get('file_id')
        obj['file_unique_id'] = obj.get('file_unique_id')
        obj['width'] = obj.get('width')
        obj['height'] = obj.get('height')
        obj['file_size'] = obj.get('file_size')
        return cls(**obj)

    def __init__(
        self,
        file_id: str,
        file_unique_id: str,
        width: int,
        height: int,
        file_size: Optional[int] = None,
        **kwargs
    ):
        _get_kwargs(self, kwargs)
        self.file_id = file_id
        self.file_unique_id = file_unique_id
        self.width = width
        self.height = height
        self.file_size = file_size


class Animation(TelegramType):
    '''
    https://core.telegram.org/bots/api#animation
    This object represents an animation file (GIF or H.264/MPEG-4 AVC video without sound).
    '''
    @classmethod
    def dese(cls, result):
        if result is None: return None
        obj = _check_dict(result)
        obj['file_id'] = obj.get('file_id')
        obj['file_unique_id'] = obj.get('file_unique_id')
        obj['width'] = obj.get('width')
        obj['height'] = obj.get('height')
        obj['duration'] = obj.get('duration')
        obj['thumbnail'] = PhotoSize.dese(obj.get('thumbnail'))
        obj['file_name'] = obj.get('file_name')
        obj['mime_type'] = obj.get('mime_type')
        obj['file_size'] = obj.get('file_size')
        return cls(**obj)

    def __init__(
        self,
        file_id: str,
        file_unique_id: str,
        width: int,
        height: int,
        duration: int,
        thumbnail: Optional[PhotoSize] = None,
        file_name: Optional[str] = None,
        mime_type: Optional[str] = None,
        file_size: Optional[int] = None,
        **kwargs
    ):
        _get_kwargs(self, kwargs)
        self.file_id = file_id
        self.file_unique_id = file_unique_id
        self.width = width
        self.height = height
        self.duration = duration
        self.thumbnail = thumbnail
        self.file_name = file_name
        self.mime_type = mime_type
        self.file_size = file_size


class Audio(TelegramType):
    '''
    https://core.telegram.org/bots/api#audio
    This object represents an audio file to be treated as music by the Telegram clients.
    '''
    @classmethod
    def dese(cls, result):
        if result is None: return None
        obj = _check_dict(result)
        obj['file_id'] = obj.get('file_id')
        obj['file_unique_id'] = obj.get('file_unique_id')
        obj['duration'] = obj.get('duration')
        obj['performer'] = obj.get('performer')
        obj['title'] = obj.get('title')
        obj['file_name'] = obj.get('file_name')
        obj['mime_type'] = obj.get('mime_type')
        obj['file_size'] = obj.get('file_size')
        obj['thumbnail'] = PhotoSize.dese(obj.get('thumbnail'))
        return cls(**obj)

    def __init__(
        self,
        file_id: str,
        file_unique_id: str,
        duration: int,
        performer: Optional[str] = None,
        title: Optional[str] = None,
        file_name: Optional[str] = None,
        mime_type: Optional[str] = None,
        file_size: Optional[int] = None,
        thumbnail: Optional[PhotoSize] = None,
        **kwargs
    ):
        _get_kwargs(self, kwargs)
        self.file_id = file_id
        self.file_unique_id = file_unique_id
        self.duration = duration
        self.performer = performer
        self.title = title
        self.file_name = file_name
        self.mime_type = mime_type
        self.file_size = file_size
        self.thumbnail = thumbnail


class Document(TelegramType):
    '''
    https://core.telegram.org/bots/api#document
    This object represents a general file (as opposed to photos, voice messages and audio files).
    '''
    @classmethod
    def dese(cls, result):
        if result is None: return None
        obj = _check_dict(result)
        obj['file_id'] = obj.get('file_id')
        obj['file_unique_id'] = obj.get('file_unique_id')
        obj['thumbnail'] = PhotoSize.dese(obj.get('thumbnail'))
        obj['file_name'] = obj.get('file_name')
        obj['mime_type'] = obj.get('mime_type')
        obj['file_size'] = obj.get('file_size')
        return cls(**obj)

    def __init__(
        self,
        file_id: str,
        file_unique_id: str,
        thumbnail: Optional[PhotoSize] = None,
        file_name: Optional[str] = None,
        mime_type: Optional[str] = None,
        file_size: Optional[int] = None,
        **kwargs
    ):
        _get_kwargs(self, kwargs)
        self.file_id = file_id
        self.file_unique_id = file_unique_id
        self.thumbnail = thumbnail
        self.file_name = file_name
        self.mime_type = mime_type
        self.file_size = file_size


class Story(TelegramType):
    '''
    https://core.telegram.org/bots/api#story
    This object represents a message about a forwarded story in the chat. Currently holds no information.
    '''
    @classmethod
    def dese(cls, result):
        if result is None: return None
        obj = _check_dict(result)
        return cls(**obj)

    def __init__(
        self,
        **kwargs
    ):
        _get_kwargs(self, kwargs)
        self.__dict__ = kwargs


class Video(TelegramType):
    '''
    https://core.telegram.org/bots/api#video
    This object represents a video file.
    '''
    @classmethod
    def dese(cls, result):
        if result is None: return None
        obj = _check_dict(result)
        obj['file_id'] = obj.get('file_id')
        obj['file_unique_id'] = obj.get('file_unique_id')
        obj['width'] = obj.get('width')
        obj['height'] = obj.get('height')
        obj['duration'] = obj.get('duration')
        obj['thumbnail'] = PhotoSize.dese(obj.get('thumbnail'))
        obj['file_name'] = obj.get('file_name')
        obj['mime_type'] = obj.get('mime_type')
        obj['file_size'] = obj.get('file_size')
        return cls(**obj)

    def __init__(
        self,
        file_id: str,
        file_unique_id: str,
        width: int,
        height: int,
        duration: int,
        thumbnail: Optional[PhotoSize] = None,
        file_name: Optional[str] = None,
        mime_type: Optional[str] = None,
        file_size: Optional[int] = None,
        **kwargs
    ):
        _get_kwargs(self, kwargs)
        self.file_id = file_id
        self.file_unique_id = file_unique_id
        self.width = width
        self.height = height
        self.duration = duration
        self.thumbnail = thumbnail
        self.file_name = file_name
        self.mime_type = mime_type
        self.file_size = file_size


class VideoNote(TelegramType):
    '''
    https://core.telegram.org/bots/api#videonote
    This object represents a video message (available in Telegram apps as of v.4.0).
    '''
    @classmethod
    def dese(cls, result):
        if result is None: return None
        obj = _check_dict(result)
        obj['file_id'] = obj.get('file_id')
        obj['file_unique_id'] = obj.get('file_unique_id')
        obj['length'] = obj.get('length')
        obj['duration'] = obj.get('duration')
        obj['thumbnail'] = PhotoSize.dese(obj.get('thumbnail'))
        obj['file_size'] = obj.get('file_size')
        return cls(**obj)

    def __init__(
        self,
        file_id: str,
        file_unique_id: str,
        length: int,
        duration: int,
        thumbnail: Optional[PhotoSize] = None,
        file_size: Optional[int] = None,
        **kwargs
    ):
        _get_kwargs(self, kwargs)
        self.file_id = file_id
        self.file_unique_id = file_unique_id
        self.length = length
        self.duration = duration
        self.thumbnail = thumbnail
        self.file_size = file_size


class Voice(TelegramType):
    '''
    https://core.telegram.org/bots/api#voice
    This object represents a voice note.
    '''
    @classmethod
    def dese(cls, result):
        if result is None: return None
        obj = _check_dict(result)
        obj['file_id'] = obj.get('file_id')
        obj['file_unique_id'] = obj.get('file_unique_id')
        obj['duration'] = obj.get('duration')
        obj['mime_type'] = obj.get('mime_type')
        obj['file_size'] = obj.get('file_size')
        return cls(**obj)

    def __init__(
        self,
        file_id: str,
        file_unique_id: str,
        duration: int,
        mime_type: Optional[str] = None,
        file_size: Optional[int] = None,
        **kwargs
    ):
        _get_kwargs(self, kwargs)
        self.file_id = file_id
        self.file_unique_id = file_unique_id
        self.duration = duration
        self.mime_type = mime_type
        self.file_size = file_size


class Contact(TelegramType):
    '''
    https://core.telegram.org/bots/api#contact
    This object represents a phone contact.
    '''
    @classmethod
    def dese(cls, result):
        if result is None: return None
        obj = _check_dict(result)
        obj['phone_number'] = obj.get('phone_number')
        obj['first_name'] = obj.get('first_name')
        obj['last_name'] = obj.get('last_name')
        obj['user_id'] = obj.get('user_id')
        obj['vcard'] = obj.get('vcard')
        return cls(**obj)

    def __init__(
        self,
        phone_number: str,
        first_name: str,
        last_name: Optional[str] = None,
        user_id: Optional[int] = None,
        vcard: Optional[str] = None,
        **kwargs
    ):
        _get_kwargs(self, kwargs)
        self.phone_number = phone_number
        self.first_name = first_name
        self.last_name = last_name
        self.user_id = user_id
        self.vcard = vcard


class Dice(TelegramType):
    '''
    https://core.telegram.org/bots/api#dice
    This object represents an animated emoji that displays a random value.
    '''
    @classmethod
    def dese(cls, result):
        if result is None: return None
        obj = _check_dict(result)
        obj['emoji'] = obj.get('emoji')
        obj['value'] = obj.get('value')
        return cls(**obj)

    def __init__(
        self,
        emoji: str,
        value: int,
        **kwargs
    ):
        _get_kwargs(self, kwargs)
        self.emoji = emoji
        self.value = value


class PollOption(TelegramType):
    '''
    https://core.telegram.org/bots/api#polloption
    This object contains information about one answer option in a poll.
    '''
    @classmethod
    def dese(cls, result):
        if result is None: return None
        obj = _check_dict(result)
        obj['text'] = obj.get('text')
        obj['voter_count'] = obj.get('voter_count')
        return cls(**obj)

    def __init__(
        self,
        text: str,
        voter_count: int,
        **kwargs
    ):
        _get_kwargs(self, kwargs)
        self.text = text
        self.voter_count = voter_count


class PollAnswer(TelegramType):
    '''
    https://core.telegram.org/bots/api#pollanswer
    This object represents an answer of a user in a non-anonymous poll.
    '''
    @classmethod
    def dese(cls, result):
        if result is None: return None
        obj = _check_dict(result)
        obj['poll_id'] = obj.get('poll_id')
        obj['option_ids'] = obj.get('option_ids')
        obj['voter_chat'] = Chat.dese(obj.get('voter_chat'))
        obj['user'] = User.dese(obj.get('user'))
        return cls(**obj)

    def __init__(
        self,
        poll_id: str,
        option_ids: list[int],
        voter_chat: Optional[Chat] = None,
        user: Optional[User] = None,
        **kwargs
    ):
        _get_kwargs(self, kwargs)
        self.poll_id = poll_id
        self.option_ids = option_ids
        self.voter_chat = voter_chat
        self.user = user


class Poll(TelegramType):
    '''
    https://core.telegram.org/bots/api#poll
    This object contains information about a poll.
    '''
    @classmethod
    def dese(cls, result):
        if result is None: return None
        obj = _check_dict(result)
        obj['id'] = obj.get('id')
        obj['question'] = obj.get('question')
        obj['options'] = [PollOption.dese(kwargs) for kwargs in obj.get('options')]
        obj['total_voter_count'] = obj.get('total_voter_count')
        obj['is_closed'] = obj.get('is_closed')
        obj['is_anonymous'] = obj.get('is_anonymous')
        obj['type'] = obj.get('type')
        obj['allows_multiple_answers'] = obj.get('allows_multiple_answers')
        obj['correct_option_id'] = obj.get('correct_option_id')
        obj['explanation'] = obj.get('explanation')
        obj['explanation_entities'] = [MessageEntity.dese(kwargs) for kwargs in obj.get('explanation_entities')] if 'explanation_entities' in obj else None
        obj['open_period'] = obj.get('open_period')
        obj['close_date'] = obj.get('close_date')
        return cls(**obj)

    def __init__(
        self,
        id: str,
        question: str,
        options: list[PollOption],
        total_voter_count: int,
        is_closed: bool,
        is_anonymous: bool,
        type: str,
        allows_multiple_answers: bool,
        correct_option_id: Optional[int] = None,
        explanation: Optional[str] = None,
        explanation_entities: Optional[list[MessageEntity]] = None,
        open_period: Optional[int] = None,
        close_date: Optional[int] = None,
        **kwargs
    ):
        _get_kwargs(self, kwargs)
        self.id = id
        self.question = question
        self.options = options
        self.total_voter_count = total_voter_count
        self.is_closed = is_closed
        self.is_anonymous = is_anonymous
        self.type = type
        self.allows_multiple_answers = allows_multiple_answers
        self.correct_option_id = correct_option_id
        self.explanation = explanation
        self.explanation_entities = explanation_entities
        self.open_period = open_period
        self.close_date = close_date


class Venue(TelegramType):
    '''
    https://core.telegram.org/bots/api#venue
    This object represents a venue.
    '''
    @classmethod
    def dese(cls, result):
        if result is None: return None
        obj = _check_dict(result)
        obj['location'] = Location.dese(obj.get('location'))
        obj['title'] = obj.get('title')
        obj['address'] = obj.get('address')
        obj['foursquare_id'] = obj.get('foursquare_id')
        obj['foursquare_type'] = obj.get('foursquare_type')
        obj['google_place_id'] = obj.get('google_place_id')
        obj['google_place_type'] = obj.get('google_place_type')
        return cls(**obj)

    def __init__(
        self,
        location: Location,
        title: str,
        address: str,
        foursquare_id: Optional[str] = None,
        foursquare_type: Optional[str] = None,
        google_place_id: Optional[str] = None,
        google_place_type: Optional[str] = None,
        **kwargs
    ):
        _get_kwargs(self, kwargs)
        self.location = location
        self.title = title
        self.address = address
        self.foursquare_id = foursquare_id
        self.foursquare_type = foursquare_type
        self.google_place_id = google_place_id
        self.google_place_type = google_place_type


class WebAppData(TelegramType):
    '''
    https://core.telegram.org/bots/api#webappdata
    Describes data sent from a Web App to the bot.
    '''
    @classmethod
    def dese(cls, result):
        if result is None: return None
        obj = _check_dict(result)
        obj['data'] = obj.get('data')
        obj['button_text'] = obj.get('button_text')
        return cls(**obj)

    def __init__(
        self,
        data: str,
        button_text: str,
        **kwargs
    ):
        _get_kwargs(self, kwargs)
        self.data = data
        self.button_text = button_text


class ProximityAlertTriggered(TelegramType):
    '''
    https://core.telegram.org/bots/api#proximityalerttriggered
    This object represents the content of a service message, sent whenever
    a user in the chat triggers a proximity alert set by another user.
    '''
    @classmethod
    def dese(cls, result):
        if result is None: return None
        obj = _check_dict(result)
        obj['traveler'] = User.dese(obj.get('traveler'))
        obj['watcher'] = User.dese(obj.get('watcher'))
        obj['distance'] = obj.get('distance')
        return cls(**obj)

    def __init__(
        self,
        traveler: User,
        watcher: User,
        distance: int,
        **kwargs
    ):
        _get_kwargs(self, kwargs)
        self.traveler = traveler
        self.watcher = watcher
        self.distance = distance


class MessageAutoDeleteTimerChanged(TelegramType):
    '''
    https://core.telegram.org/bots/api#messageautodeletetimerchanged
    This object represents a service message about a change in auto-delete timer settings.
    '''
    @classmethod
    def dese(cls, result):
        if result is None: return None
        obj = _check_dict(result)
        obj['message_auto_delete_time'] = obj.get('message_auto_delete_time')
        return cls(**obj)

    def __init__(
        self,
        message_auto_delete_time: int,
        **kwargs
    ):
        _get_kwargs(self, kwargs)
        self.message_auto_delete_time = message_auto_delete_time


class ForumTopicCreated(TelegramType):
    '''
    https://core.telegram.org/bots/api#forumtopiccreated
    This object represents a service message about a new forum topic created in the chat.
    '''
    @classmethod
    def dese(cls, result):
        if result is None: return None
        obj = _check_dict(result)
        obj['name'] = obj.get('name')
        obj['icon_color'] = obj.get('icon_color')
        obj['icon_custom_emoji_id'] = obj.get('icon_custom_emoji_id')
        return cls(**obj)

    def __init__(
        self,
        name: str,
        icon_color: int,
        icon_custom_emoji_id: Optional[str] = None,
        **kwargs
    ):
        _get_kwargs(self, kwargs)
        self.name = name
        self.icon_color = icon_color
        self.icon_custom_emoji_id = icon_custom_emoji_id


class ForumTopicClosed(TelegramType):
    '''
    https://core.telegram.org/bots/api#forumtopicclosed
    This object represents a service message about a forum
    topic closed in the chat. Currently holds no information.
    '''
    @classmethod
    def dese(cls, result):
        if result is None: return None
        obj = _check_dict(result)
        return cls(**obj)

    def __init__(
        self,
        **kwargs
    ):
        _get_kwargs(self, kwargs)
        self.__dict__ = kwargs


class ForumTopicEdited(TelegramType):
    '''
    https://core.telegram.org/bots/api#forumtopicedited
    This object represents a service message about an edited forum topic.
    '''
    @classmethod
    def dese(cls, result):
        if result is None: return None
        obj = _check_dict(result)
        obj['name'] = obj.get('name')
        obj['icon_custom_emoji_id'] = obj.get('icon_custom_emoji_id')
        return cls(**obj)

    def __init__(
        self,
        name: Optional[str] = None,
        icon_custom_emoji_id: Optional[str] = None,
        **kwargs
    ):
        _get_kwargs(self, kwargs)
        self.name = name
        self.icon_custom_emoji_id = icon_custom_emoji_id


class ForumTopicReopened(TelegramType):
    '''
    https://core.telegram.org/bots/api#forumtopicreopened
    This object represents a service message about a forum
    topic reopened in the chat. Currently holds no information.
    '''
    @classmethod
    def dese(cls, result):
        if result is None: return None
        obj = _check_dict(result)
        return cls(**obj)

    def __init__(
        self,
        **kwargs
    ):
        _get_kwargs(self, kwargs)
        self.__dict__ = kwargs


class GeneralForumTopicHidden(TelegramType):
    '''
    https://core.telegram.org/bots/api#generalforumtopichidden
    This object represents a service message about General forum
    topic hidden in the chat. Currently holds no information.
    '''
    @classmethod
    def dese(cls, result):
        if result is None: return None
        obj = _check_dict(result)
        return cls(**obj)

    def __init__(
        self,
        **kwargs
    ):
        _get_kwargs(self, kwargs)
        self.__dict__ = kwargs


class GeneralForumTopicUnhidden(TelegramType):
    '''
    https://core.telegram.org/bots/api#generalforumtopicunhidden
    This object represents a service message about General forum
    topic unhidden in the chat. Currently holds no information.
    '''
    @classmethod
    def dese(cls, result):
        if result is None: return None
        obj = _check_dict(result)
        return cls(**obj)

    def __init__(
        self,
        **kwargs
    ):
        _get_kwargs(self, kwargs)
        self.__dict__ = kwargs


class UsersShared(TelegramType):
    '''
    https://core.telegram.org/bots/api#usersshared
    This object contains information about the users whose identifiers
    were shared with the bot using a KeyboardButtonRequestUsers button.
    '''
    @classmethod
    def dese(cls, result):
        if result is None: return None
        obj = _check_dict(result)
        obj['request_id'] = obj.get('request_id')
        obj['user_ids'] = obj.get('user_ids')
        return cls(**obj)

    def __init__(
        self,
        request_id: int,
        user_ids: list[int],
        **kwargs
    ):
        _get_kwargs(self, kwargs)
        self.request_id = request_id
        self.user_ids = user_ids


class ChatShared(TelegramType):
    '''
    https://core.telegram.org/bots/api#chatshared
    This object contains information about the chat whose identifier
    was shared with the bot using a KeyboardButtonRequestChat button.
    '''
    @classmethod
    def dese(cls, result):
        if result is None: return None
        obj = _check_dict(result)
        obj['request_id'] = obj.get('request_id')
        obj['chat_id'] = obj.get('chat_id')
        return cls(**obj)

    def __init__(
        self,
        request_id: int,
        chat_id: int,
        **kwargs
    ):
        _get_kwargs(self, kwargs)
        self.request_id = request_id
        self.chat_id = chat_id


class WriteAccessAllowed(TelegramType):
    '''
    https://core.telegram.org/bots/api#writeaccessallowed
    This object represents a service message about a user allowing a bot to write
    messages after adding it to the attachment menu, launching a Web App from a link,
    or accepting an explicit request from a Web App sent by the method requestWriteAccess.
    '''
    @classmethod
    def dese(cls, result):
        if result is None: return None
        obj = _check_dict(result)
        obj['from_request'] = obj.get('from_request')
        obj['web_app_name'] = obj.get('web_app_name')
        obj['from_attachment_menu'] = obj.get('from_attachment_menu')
        return cls(**obj)

    def __init__(
        self,
        from_request: Optional[bool] = None,
        web_app_name: Optional[str] = None,
        from_attachment_menu: Optional[bool] = None,
        **kwargs
    ):
        _get_kwargs(self, kwargs)
        self.from_request = from_request
        self.web_app_name = web_app_name
        self.from_attachment_menu = from_attachment_menu


class VideoChatScheduled(TelegramType):
    '''
    https://core.telegram.org/bots/api#videochatscheduled
    This object represents a service message about a video chat scheduled in the chat.
    '''
    @classmethod
    def dese(cls, result):
        if result is None: return None
        obj = _check_dict(result)
        obj['start_date'] = obj.get('start_date')
        return cls(**obj)

    def __init__(
        self,
        start_date: int,
        **kwargs
    ):
        _get_kwargs(self, kwargs)
        self.start_date = start_date


class VideoChatStarted(TelegramType):
    '''
    https://core.telegram.org/bots/api#videochatstarted
    This object represents a service message about a video
    chat started in the chat. Currently holds no information.
    '''
    @classmethod
    def dese(cls, result):
        if result is None: return None
        obj = _check_dict(result)
        return cls(**obj)

    def __init__(
        self,
        **kwargs
    ):
        _get_kwargs(self, kwargs)
        self.__dict__ = kwargs


class VideoChatEnded(TelegramType):
    '''
    https://core.telegram.org/bots/api#videochatended
    This object represents a service message about a video chat ended in the chat.
    '''
    @classmethod
    def dese(cls, result):
        if result is None: return None
        obj = _check_dict(result)
        obj['duration'] = obj.get('duration')
        return cls(**obj)

    def __init__(
        self,
        duration: int,
        **kwargs
    ):
        _get_kwargs(self, kwargs)
        self.duration = duration


class VideoChatParticipantsInvited(TelegramType):
    '''
    https://core.telegram.org/bots/api#videochatparticipantsinvited
    This object represents a service message about new members invited to a video chat.
    '''
    @classmethod
    def dese(cls, result):
        if result is None: return None
        obj = _check_dict(result)
        obj['users'] = [User.dese(kwargs) for kwargs in obj.get('users')]
        return cls(**obj)

    def __init__(
        self,
        users: list[User],
        **kwargs
    ):
        _get_kwargs(self, kwargs)
        self.users = users


class UserProfilePhotos(TelegramType):
    '''
    https://core.telegram.org/bots/api#userprofilephotos
    This object represent a user's profile pictures.
    '''
    @classmethod
    def dese(cls, result):
        if result is None: return None
        obj = _check_dict(result)
        obj['total_count'] = obj.get('total_count')
        obj['photos'] = [[PhotoSize.dese(kwargs) for kwargs in lst] for lst in obj.get('photos')]
        return cls(**obj)

    def __init__(
        self,
        total_count: int,
        photos: list[list[PhotoSize]],
        **kwargs
    ):
        _get_kwargs(self, kwargs)
        self.total_count = total_count
        self.photos = photos


class File(TelegramType):
    '''
    https://core.telegram.org/bots/api#file
    This object represents a file ready to be downloaded. The file can be downloaded via the link
    https://api.telegram.org/file/bot<token>/<file_path>. It is guaranteed that the link will be
    valid for at least 1 hour. When the link expires, a new one can be requested by calling getFile.
    '''
    @classmethod
    def dese(cls, result):
        if result is None: return None
        obj = _check_dict(result)
        obj['file_id'] = obj.get('file_id')
        obj['file_unique_id'] = obj.get('file_unique_id')
        obj['file_size'] = obj.get('file_size')
        obj['file_path'] = obj.get('file_path')
        return cls(**obj)

    def __init__(
        self,
        file_id: str,
        file_unique_id: str,
        file_size: Optional[int] = None,
        file_path: Optional[str] = None,
        **kwargs
    ):
        _get_kwargs(self, kwargs)
        self.file_id = file_id
        self.file_unique_id = file_unique_id
        self.file_size = file_size
        self.file_path = file_path


class WebAppInfo(TelegramType):
    '''
    https://core.telegram.org/bots/api#webappinfo
    Describes a Web App.
    '''
    @classmethod
    def dese(cls, result):
        if result is None: return None
        obj = _check_dict(result)
        obj['url'] = obj.get('url')
        return cls(**obj)

    def __init__(
        self,
        url: str
    ):
        self.url = url


class KeyboardButtonRequestUsers(TelegramType):
    '''
    https://core.telegram.org/bots/api#keyboardbuttonrequestusers
    This object defines the criteria used to request suitable users. The identifiers of
    the selected users will be shared with the bot when the corresponding button is pressed.
    '''
    def __init__(
        self,
        request_id: int,
        user_is_bot: Optional[bool] = None,
        user_is_premium: Optional[bool] = None,
        max_quantity: Optional[int] = None
    ):
        self.request_id = request_id
        self.user_is_bot = user_is_bot
        self.user_is_premium = user_is_premium
        self.max_quantity = max_quantity


class KeyboardButtonRequestChat(TelegramType):
    '''
    https://core.telegram.org/bots/api#keyboardbuttonrequestchat
    This object defines the criteria used to request a suitable chat. The identifier of
    the selected chat will be shared with the bot when the corresponding button is pressed.
    '''
    def __init__(
        self,
        request_id: int,
        chat_is_channel: bool,
        chat_is_forum: Optional[bool] = None,
        chat_has_username: Optional[bool] = None,
        chat_is_created: Optional[bool] = None,
        user_administrator_rights: Optional[ChatAdministratorRights] = None,
        bot_administrator_rights: Optional[ChatAdministratorRights] = None,
        bot_is_member: Optional[bool] = None
    ):
        self.request_id = request_id
        self.chat_is_channel = chat_is_channel
        self.chat_is_forum = chat_is_forum
        self.chat_has_username = chat_has_username
        self.chat_is_created = chat_is_created
        self.user_administrator_rights = user_administrator_rights
        self.bot_administrator_rights = bot_administrator_rights
        self.bot_is_member = bot_is_member


class KeyboardButtonPollType(TelegramType):
    '''
    https://core.telegram.org/bots/api#keyboardbuttonpolltype
    This object represents type of a poll, which is allowed to
    be created and sent when the corresponding button is pressed.
    '''
    def __init__(
        self,
        type: Optional[str] = None
    ):
        self.type = type


class KeyboardButton(TelegramType):
    '''
    https://core.telegram.org/bots/api#keyboardbutton
    This object represents one button of the reply keyboard. For
    simple text buttons, String can be used instead of this object to specify
    the button text. The optional fields web_app, request_users, request_chat,
    request_contact, request_location, and request_poll are mutually exclusive.
    '''
    def __init__(
        self,
        text: str,
        request_users: Optional[KeyboardButtonRequestUsers] = None,
        request_chat: Optional[KeyboardButtonRequestChat] = None,
        request_contact: Optional[bool] = None,
        request_location: Optional[bool] = None,
        request_poll: Optional[KeyboardButtonPollType] = None,
        web_app: Optional[WebAppInfo] = None
    ):
        self.text = text
        self.request_users = request_users
        self.request_chat = request_chat
        self.request_contact = request_contact
        self.request_location = request_location
        self.request_poll = request_poll
        self.web_app = web_app


class ReplyKeyboardMarkup(TelegramType):
    '''
    https://core.telegram.org/bots/api#replykeyboardmarkup
    This object represents a custom keyboard with reply
    options (see Introduction to bots for details and examples).
    '''
    def __init__(
        self,
        keyboard: Optional[list[list[KeyboardButton]]] = None,
        is_persistent: Optional[bool] = None,
        resize_keyboard: Optional[bool] = None,
        one_time_keyboard: Optional[bool] = None,
        input_field_placeholder: Optional[str] = None,
        selective: Optional[bool] = None
    ):
        self.keyboard = [] if keyboard is None else keyboard
        self.is_persistent = is_persistent
        self.resize_keyboard = resize_keyboard
        self.one_time_keyboard = one_time_keyboard
        self.input_field_placeholder = input_field_placeholder
        self.selective = selective

    def add(self, *buttons: KeyboardButton):
        self.keyboard.append(buttons)
        return self

    @property
    def row_width(self) -> int:
        return len(self.keyboard)

    @row_width.setter
    def row_width(self, value: int) -> int:

        keyboard = []
        nested = []
        for row in self.keyboard:
            for button in row:
                nested.append(button)
                if len(nested) == value:
                    keyboard.append(nested)
                    nested = []

        if nested != []:
            keyboard.append(nested)

        self.keyboard = keyboard
        return self.row_width


class ReplyKeyboardRemove(TelegramType):
    '''
    https://core.telegram.org/bots/api#replykeyboardremove
    Upon receiving a message with this object, Telegram clients will remove the current
    custom keyboard and display the default letter-keyboard. By default, custom keyboards
    are displayed until a new keyboard is sent by a bot. An exception is made for one-time
    keyboards that are hidden immediately after the user presses a button (see ReplyKeyboardMarkup).
    '''
    def __init__(
        self,
        remove_keyboard: Literal[True] = True,
        selective: Optional[bool] = None
    ):
        self.remove_keyboard = remove_keyboard
        self.selective = selective


class InlineKeyboardButton(TelegramType):
    '''
    https://core.telegram.org/bots/api#inlinekeyboardbutton
    This object represents one button of an inline keyboard. You must use exactly one of the optional fields.
    '''
    @classmethod
    def dese(cls, result):
        if result is None: return None
        obj = _check_dict(result)
        obj['text'] = obj.get('text')
        obj['url'] = obj.get('url')
        obj['callback_data'] = obj.get('callback_data')
        obj['web_app'] = WebAppInfo.dese(obj.get('web_app'))
        obj['login_url'] = LoginUrl.dese(obj.get('login_url'))
        obj['switch_inline_query'] = obj.get('switch_inline_query')
        obj['switch_inline_query_current_chat'] = obj.get('switch_inline_query_current_chat')
        obj['switch_inline_query_chosen_chat'] = SwitchInlineQueryChosenChat.dese(obj.get('switch_inline_query_chosen_chat'))
        obj['callback_game'] = CallbackGame.dese(obj.get('callback_game'))
        obj['pay'] = obj.get('pay')
        return cls(**obj)

    def __init__(
        self,
        text: str,
        url: Optional[str] = None,
        callback_data: Optional[str] = None,
        web_app: Optional[WebAppInfo] = None, 
        login_url: Optional[LoginUrl] = None,
        switch_inline_query: Optional[str] = None,
        switch_inline_query_current_chat: Optional[str] = None,
        switch_inline_query_chosen_chat: Optional[SwitchInlineQueryChosenChat] = None,
        callback_game: Optional[CallbackGame] = None,
        pay: Optional[bool] = None
    ):
        self.text = text
        self.url = url
        self.callback_data = callback_data
        self.web_app = web_app
        self.login_url = login_url
        self.switch_inline_query = switch_inline_query
        self.switch_inline_query_current_chat = switch_inline_query_current_chat
        self.switch_inline_query_chosen_chat = switch_inline_query_chosen_chat
        self.callback_game = callback_game
        self.pay = pay


class InlineKeyboardMarkup(TelegramType):
    '''
    https://core.telegram.org/bots/api#inlinekeyboardmarkup
    This object represents an inline keyboard that appears right next to the message it belongs to.
    '''
    @classmethod
    def dese(cls, result):
        if result is None: return None
        obj = _check_dict(result)
        obj['inline_keyboard'] = [[InlineKeyboardButton.dese(kwargs) for kwargs in lst] for lst in obj.get('inline_keyboard')]
        return cls(**obj)

    def __init__(
        self,
        inline_keyboard: Optional[list[list[InlineKeyboardButton]]] = None
    ):
        self.inline_keyboard = [] if inline_keyboard is None else inline_keyboard

    def add(self, *buttons: InlineKeyboardButton):
        self.inline_keyboard.append(buttons)
        return self

    @property
    def row_width(self) -> int:
        return len(self.inline_keyboard)

    @row_width.setter
    def row_width(self, value: int) -> int:

        keyboard = []
        nested = []
        for row in self.inline_keyboard:
            for button in row:
                nested.append(button)
                if len(nested) == value:
                    keyboard.append(nested)
                    nested = []

        if nested != []:
            keyboard.append(nested)

        self.inline_keyboard = keyboard
        return self.row_width


class CallbackQuery(TelegramType):
    '''
    https://core.telegram.org/bots/api#callbackquery
    This object represents an incoming callback query from a callback button in
    an inline keyboard. If the button that originated the query was attached to a
    message sent by the bot, the field message will be present. If the button was
    attached to a message sent via the bot (in inline mode), the field inline_message_id
    will be present. Exactly one of the fields data or game_short_name will be present.
    '''
    @classmethod
    def dese(cls, result):
        if result is None: return None
        obj = _check_dict(result)
        obj['id'] = obj.get('id')
        obj['from_user'] = User.dese(obj.get('from_user'))
        obj['message'] = MaybeInaccessibleMessage.dese(obj.get('message'))
        obj['inline_message_id'] = obj.get('inline_message_id')
        obj['chat_instance'] = obj.get('chat_instance')
        obj['data'] = obj.get('data')
        obj['game_short_name'] = obj.get('game_short_name')
        return cls(**obj)

    def __init__(
        self,
        id: str,
        from_user: User,
        chat_instance: str,
        message: Optional[MaybeInaccessibleMessage] = None,
        inline_message_id: str = None,
        data: Optional[str] = None,
        game_short_name: Optional[str] = None,
        **kwargs
    ):
        _get_kwargs(self, kwargs)
        self.id = id
        self.from_user = from_user
        self.chat_instance = chat_instance
        self.message = message
        self.inline_message_id = inline_message_id
        self.data = data
        self.game_short_name = game_short_name


class ForceReply(TelegramType):
    '''
    https://core.telegram.org/bots/api#forcereply
    Upon receiving a message with this object, Telegram clients will display a reply interface to
    the user (act as if the user has selected the bot's message and tapped 'Reply'). This can be extremely
    useful if you want to create user-friendly step-by-step interfaces without having to sacrifice privacy mode.
    '''
    def __init__(
        self,
        force_reply: Literal[True] = True,
        input_field_placeholder: Optional[str] = None,
        selective: Optional[bool] = None
    ):
        self.force_reply = force_reply
        self.input_field_placeholder = input_field_placeholder
        self.selective = selective


class ChatInviteLink(TelegramType):
    '''
    https://core.telegram.org/bots/api#chatinvitelink
    Represents an invite link for a chat.
    '''
    @classmethod
    def dese(cls, result):
        if result is None: return None
        obj = _check_dict(result)
        obj['invite_link'] = obj.get('invite_link')
        obj['creator'] = User.dese(obj.get('creator'))
        obj['creates_join_request'] = obj.get('creates_join_request')
        obj['is_primary'] = obj.get('is_primary')
        obj['is_revoked'] = obj.get('is_revoked')
        obj['name'] = obj.get('name')
        obj['expire_date'] = obj.get('expire_date')
        obj['member_limit'] = obj.get('member_limit')
        obj['pending_join_request_count'] = obj.get('pending_join_request_count')
        return cls(**obj)

    def __init__(
        self,
        invite_link: str,
        creator: User,
        creates_join_request: bool,
        is_primary: bool,
        is_revoked: bool,
        name: Optional[str] = None,
        expire_date: Optional[int] = None,
        member_limit: Optional[int] = None,
        pending_join_request_count: Optional[int] = None,
        **kwargs
    ):
        _get_kwargs(self, kwargs)
        self.invite_link = invite_link
        self.creator = creator
        self.creates_join_request = creates_join_request
        self.is_primary = is_primary
        self.is_revoked = is_revoked
        self.name = name
        self.expire_date = expire_date
        self.member_limit = member_limit
        self.pending_join_request_count = pending_join_request_count


# ChatMember: 6 SUBCLASSES

class ChatMember(TelegramType):
    '''
    https://core.telegram.org/bots/api#chatmember
    This object contains information about one member of a chat.
    Currently, the following 6 types of chat members are supported:
    - ChatMemberOwner
    - ChatMemberAdministrator
    - ChatMemberMember
    - ChatMemberRestricted
    - ChatMemberLeft
    - ChatMemberBanned
    '''
    @classmethod
    def dese(cls, result):
        if result is None: return None
        obj = _check_dict(result)        
        obj['user'] = User.dese(obj.get('user'))

        status = obj['status']

        if status == 'creator':
            return ChatMemberOwner(**obj)

        elif status == 'administrator':
            return ChatMemberAdministrator(**obj)

        elif status == 'member':
            return ChatMemberMember(**obj)

        elif status == 'restricted':
            return ChatMemberRestricted(**obj)

        elif status == 'left':
            return ChatMemberLeft(**obj)

        elif status == 'kicked':
            return ChatMemberBanned(**obj)
        else:
            return cls(**obj)

    def __init__(
        self,
        **kwargs
    ):
        members = ', '.join([
            ChatMemberOwner.__name__,
            ChatMemberAdministrator.__name__,
            ChatMemberMember.__name__,
            ChatMemberRestricted.__name__,
            ChatMemberLeft.__name__,
            ChatMemberBanned.__name__
        ])
        logger.warning(
            'ChatMember warning, expected one'
            f' of the following types: {members}.'
        )
        self.__dict__ = kwargs


class ChatMemberOwner(ChatMember):
    '''
    https://core.telegram.org/bots/api#chatmemberowner
    Represents a chat member that owns the chat and has all administrator privileges.
    '''
    def __init__(
        self,
        status: str,
        user: User,
        is_anonymous: bool,
        custom_title: Optional[str] = None,
        **kwargs
    ):
        _get_kwargs(self, kwargs)
        self.status = status
        self.user = user
        self.is_anonymous = is_anonymous
        self.custom_title = custom_title


class ChatMemberAdministrator(ChatMember):
    '''
    https://core.telegram.org/bots/api#chatmemberadministrator
    Represents a chat member that has some additional privileges.
    '''
    def __init__(
        self,
        status: str,
        user: User,
        can_be_edited: bool,
        is_anonymous: bool,
        can_manage_chat: bool,
        can_delete_messages: bool,
        can_manage_video_chats: bool,
        can_restrict_members: bool,
        can_promote_members: bool,
        can_change_info: bool,
        can_invite_users: bool,
        can_post_messages: Optional[bool] = None,
        can_edit_messages: Optional[bool] = None,
        can_pin_messages: Optional[bool] = None,
        can_post_stories: Optional[bool] = None,
        can_edit_stories: Optional[bool] = None,
        can_delete_stories: Optional[bool] = None,
        can_manage_topics: Optional[bool] = None,
        custom_title: Optional[str] = None,
        **kwargs
    ):
        _get_kwargs(self, kwargs)
        self.status = status
        self.user = user
        self.can_be_edited = can_be_edited
        self.is_anonymous = is_anonymous
        self.can_manage_chat = can_manage_chat
        self.can_delete_messages = can_delete_messages
        self.can_manage_video_chats = can_manage_video_chats
        self.can_restrict_members = can_restrict_members
        self.can_promote_members = can_promote_members
        self.can_change_info = can_change_info
        self.can_invite_users = can_invite_users
        self.can_post_messages = can_post_messages
        self.can_edit_messages = can_edit_messages
        self.can_pin_messages = can_pin_messages
        self.can_post_stories = can_post_stories
        self.can_edit_stories = can_edit_stories
        self.can_delete_stories = can_delete_stories
        self.can_manage_topics = can_manage_topics
        self.custom_title = custom_title


class ChatMemberMember(ChatMember):
    '''
    https://core.telegram.org/bots/api#chatmembermember
    Represents a chat member that has no additional privileges or restrictions.
    '''
    def __init__(
        self,
        status: str,
        user: User,
        **kwargs
    ):
        _get_kwargs(self, kwargs)
        self.status = status
        self.user = user


class ChatMemberRestricted(ChatMember):
    '''
    https://core.telegram.org/bots/api#chatmemberrestricted
    Represents a chat member that is under certain restrictions in the chat. Supergroups only.
    '''
    def __init__(
        self,
        status: str,
        user: User,
        is_member: bool,
        can_send_messages: bool,
        can_send_audios: bool,
        can_send_documents: bool,
        can_send_photos: bool,
        can_send_videos: bool,
        can_send_video_notes: bool,
        can_send_voice_notes: bool,
        can_send_polls: bool,
        can_send_other_messages: bool,
        can_add_web_page_previews: bool,
        can_change_info: bool,
        can_invite_users: bool,
        can_pin_messages: bool,
        can_manage_topics: bool,
        until_date: int,
        **kwargs
    ):
        _get_kwargs(self, kwargs)
        self.status = status
        self.user = user
        self.is_member = is_member
        self.can_send_messages = can_send_messages
        self.can_send_audios = can_send_audios
        self.can_send_documents = can_send_documents
        self.can_send_photos = can_send_photos
        self.can_send_videos = can_send_videos
        self.can_send_video_notes = can_send_video_notes
        self.can_send_voice_notes = can_send_voice_notes
        self.can_send_polls = can_send_polls
        self.can_send_other_messages = can_send_other_messages
        self.can_add_web_page_previews = can_add_web_page_previews
        self.can_change_info = can_change_info
        self.can_invite_users = can_invite_users
        self.can_pin_messages = can_pin_messages
        self.can_manage_topics = can_manage_topics
        self.until_date = until_date


class ChatMemberLeft(ChatMember):
    '''
    https://core.telegram.org/bots/api#chatmemberleft
    Represents a chat member that isn't currently a member of the chat, but may join it themselves.
    '''
    def __init__(
        self,
        status: str,
        user: User,
        **kwargs
    ):
        _get_kwargs(self, kwargs)
        self.status = status
        self.user = user


class ChatMemberBanned(ChatMember):
    '''
    https://core.telegram.org/bots/api#chatmemberbanned
    Represents a chat member that was banned in the chat and can't return to the chat or view chat messages.
    '''
    def __init__(
        self,
        status: str,
        user: User,
        until_date: int,
        **kwargs
    ):
        _get_kwargs(self, kwargs)
        self.status = status
        self.user = user
        self.until_date = until_date


class ChatMemberUpdated(TelegramType):
    '''
    https://core.telegram.org/bots/api#chatmemberupdated
    This object represents changes in the status of a chat member.
    '''
    @classmethod
    def dese(cls, result):
        if result is None: return None
        obj = _check_dict(result)
        obj['chat'] = Chat.dese(obj.get('chat'))
        obj['from_user'] = User.dese(obj.get('from_user'))
        obj['date'] = obj.get('date')
        obj['old_chat_member'] = ChatMember.dese(obj.get('old_chat_member'))
        obj['new_chat_member'] = ChatMember.dese(obj.get('new_chat_member'))
        obj['invite_link'] = ChatInviteLink.dese(obj.get('invite_link'))
        obj['via_chat_folder_invite_link'] = obj.get('via_chat_folder_invite_link')
        return cls(**obj)

    def __init__(
        self,
        chat: Chat,
        from_user: User,
        date: int,
        old_chat_member: ChatMember,
        new_chat_member: ChatMember,
        invite_link: Optional[ChatInviteLink] = None,
        via_chat_folder_invite_link: Optional[bool] = None,
        **kwargs
    ):
        _get_kwargs(self, kwargs)
        self.chat = chat
        self.from_user = from_user
        self.date = date
        self.old_chat_member = old_chat_member
        self.new_chat_member = new_chat_member
        self.invite_link = invite_link
        self.via_chat_folder_invite_link = via_chat_folder_invite_link


class ChatJoinRequest(TelegramType):
    '''
    https://core.telegram.org/bots/api#chatjoinrequest
    Represents a join request sent to a chat.
    '''
    @classmethod
    def dese(cls, result):
        if result is None: return None
        obj = _check_dict(result)
        obj['chat'] = Chat.dese(obj.get('chat'))
        obj['from_user'] = User.dese(obj.get('from_user'))
        obj['user_chat_id'] = obj.get('user_chat_id')
        obj['date'] = obj.get('date')
        obj['bio'] = obj.get('bio')
        obj['invite_link'] = ChatInviteLink.dese(obj.get('invite_link'))
        return cls(**obj)

    def __init__(
        self,
        chat: Chat,
        from_user: User,
        user_chat_id: int,
        date: int,
        bio: Optional[str] = None,
        invite_link: Optional[ChatInviteLink] = None,
        **kwargs
    ):
        _get_kwargs(self, kwargs)
        self.chat = chat
        self.from_user = from_user
        self.user_chat_id = user_chat_id
        self.date = date
        self.bio = bio
        self.invite_link = invite_link


class ForumTopic(TelegramType):
    '''
    Represents a location to which a chat is connected.
    This object represents a forum topic.
    '''
    @classmethod
    def dese(cls, result):
        if result is None: return None
        obj = _check_dict(result)
        obj['message_thread_id'] = obj.get('message_thread_id')
        obj['name'] = obj.get('name')
        obj['icon_color'] = obj.get('icon_color')
        obj['icon_custom_emoji_id'] = obj.get('icon_custom_emoji_id')
        return cls(**obj)

    def __init__(
        self,
        message_thread_id: int,
        name: str,
        icon_color: int,
        icon_custom_emoji_id: Optional[str] = None,
        **kwargs
    ):
        _get_kwargs(self, kwargs)
        self.message_thread_id = message_thread_id
        self.name = name
        self.icon_color = icon_color
        self.icon_custom_emoji_id = icon_custom_emoji_id


class BotCommand(TelegramType):
    '''
    https://core.telegram.org/bots/api#botcommand
    This object represents a bot command.
    '''
    @classmethod
    def dese(cls, result):
        if result is None: return None
        obj = _check_dict(result)
        obj['command'] = obj.get('command')
        obj['description'] = obj.get('description')
        return cls(**obj)

    def __init__(
        self,
        command: str,
        description: str
    ):
        self.command = command
        self.description = description


# BotCommandScope: 7 SUBCLASSES

class BotCommandScope(TelegramType):
    '''
    https://core.telegram.org/bots/api#botcommandscope
    This object represents the scope to which bot commands are applied. Currently, the following 7 scopes are supported:
    - BotCommandScopeDefault
    - BotCommandScopeAllPrivateChats
    - BotCommandScopeAllGroupChats
    - BotCommandScopeAllChatAdministrators
    - BotCommandScopeChat
    - BotCommandScopeChatAdministrators
    - BotCommandScopeChatMember
    '''
    def __init__(
        self,
        **kwargs
    ):
        scopes = ', '.join([
            BotCommandScopeDefault.__name__,
            BotCommandScopeAllPrivateChats.__name__,
            BotCommandScopeAllGroupChats.__name__,
            BotCommandScopeAllChatAdministrators.__name__,
            BotCommandScopeChat.__name__,
            BotCommandScopeChatAdministrators.__name__,
            BotCommandScopeChatMember.__name__
        ])
        logger.warning(
            'BotCommandScope warning, expected one'
            f' of the following types: {scopes}.'
        )
        self.__dict__ = kwargs


class BotCommandScopeDefault(BotCommandScope):
    '''
    https://core.telegram.org/bots/api#botcommandscopedefault
    Represents the default scope of bot commands. Default commands are
    used if no commands with a narrower scope are specified for the user.
    '''
    def __init__(
        self,
        type: str = 'default'
    ):
        self.type = type


class BotCommandScopeAllPrivateChats(BotCommandScope):
    '''
    https://core.telegram.org/bots/api#botcommandscopeallprivatechats
    Represents the scope of bot commands, covering all private chats.
    '''
    def __init__(
        self,
        type: str = 'all_private_chats'
    ):
        self.type = type


class BotCommandScopeAllGroupChats(BotCommandScope):
    '''
    https://core.telegram.org/bots/api#botcommandscopeallgroupchats
    Represents the scope of bot commands, covering all group and supergroup chats.
    '''
    def __init__(
        self,
        type: str = 'all_group_chats'
    ):
        self.type = type


class BotCommandScopeAllChatAdministrators(BotCommandScope):
    '''
    https://core.telegram.org/bots/api#botcommandscopeallchatadministrators
    Represents the scope of bot commands, covering all group and supergroup chat administrators.
    '''
    def __init__(
        self,
        type: str = 'all_chat_administrators'
    ):
        self.type = type


class BotCommandScopeChat(BotCommandScope):
    '''
    https://core.telegram.org/bots/api#botcommandscopechat
    Represents the scope of bot commands, covering a specific chat.
    '''
    def __init__(
        self,
        chat_id: Union[int, str],
        type: str = 'chat'
    ):
        self.type = type
        self.chat_id = chat_id


class BotCommandScopeChatAdministrators(BotCommandScope):
    '''
    https://core.telegram.org/bots/api#botcommandscopechatadministrators
    Represents the scope of bot commands, covering all administrators of a specific group or supergroup chat.
    '''
    def __init__(
        self,
        chat_id: Union[int, str],
        type: str = 'chat_administrators'
    ):
        self.type = type
        self.chat_id = chat_id


class BotCommandScopeChatMember(BotCommandScope):
    '''
    https://core.telegram.org/bots/api#botcommandscopechatmember
    Represents the scope of bot commands, covering a specific member of a group or supergroup chat.
    '''
    def __init__(
        self,
        chat_id: Union[int, str],
        user_id: int,
        type: str = 'chat_member'
    ):
        self.type = type
        self.chat_id = chat_id
        self.user_id = user_id


class BotName(TelegramType):
    '''
    https://core.telegram.org/bots/api#botname
    This object represents the bot's name.
    '''
    @classmethod
    def dese(cls, result):
        if result is None: return None
        obj = _check_dict(result)
        obj['name'] = obj.get('name')
        return cls(**obj)

    def __init__(
        self,
        name: str,
        **kwargs
    ):
        _get_kwargs(self, kwargs)
        self.name = name


class BotDescription(TelegramType):
    '''
    https://core.telegram.org/bots/api#botdescription
    This object represents the bot's description.
    '''
    @classmethod
    def dese(cls, result):
        if result is None: return None
        obj = _check_dict(result)
        obj['description'] = obj.get('description')
        return cls(**obj)

    def __init__(
        self,
        description: str,
        **kwargs
    ):
        _get_kwargs(self, kwargs)
        self.description = description


class BotShortDescription(TelegramType):
    '''
    https://core.telegram.org/bots/api#botshortdescription
    This object represents the bot's short description.
    '''
    @classmethod
    def dese(cls, result):
        if result is None: return None
        obj = _check_dict(result)
        obj['short_description'] = obj.get('short_description')
        return cls(**obj)

    def __init__(
        self,
        short_description: str,
        **kwargs
    ):
        _get_kwargs(self, kwargs)
        self.short_description = short_description


# MenuButton: 3 SUBCLASSES

class MenuButton(TelegramType):
    '''
    https://core.telegram.org/bots/api#menubutton
    This object describes the bot's menu button in a private chat. It should be one of
    - MenuButtonCommands
    - MenuButtonWebApp
    - MenuButtonDefault
    If a menu button other than MenuButtonDefault is set for a private chat, then it is applied in the chat.
    Otherwise the default menu button is applied. By default, the menu button opens the list of bot commands.
    '''
    @classmethod
    def dese(cls, result):
        if result is None: return None
        obj = _check_dict(result)
        type = obj['type']

        if type == 'commands':
            return MenuButtonCommands(**obj)

        elif type == 'web_app':
            obj['web_app'] = WebAppInfo.dese(obj.get('web_app'))
            return MenuButtonWebApp(**obj)

        elif type == 'default':
            return MenuButtonDefault(**obj)
        else:
            return cls(**obj)

    def __init__(
        self,
        **kwargs
    ):
        menus = ', '.join([
            MenuButtonCommands.__name__,
            MenuButtonWebApp.__name__,
            MenuButtonDefault.__name__
        ])
        logger.warning(
            'MenuButton warning, expected one'
            f' of the following types: {menus}.'
        )
        self.__dict__ = kwargs


class MenuButtonCommands(MenuButton):
    '''
    https://core.telegram.org/bots/api#menubuttoncommands
    Represents a menu button, which opens the bot's list of commands.
    '''
    def __init__(
        self,
        type: str = 'commands'
    ):
        self.type = type


class MenuButtonWebApp(MenuButton):
    '''
    https://core.telegram.org/bots/api#menubuttonwebapp
    Represents a menu button, which launches a Web App.
    '''
    def __init__(
        self,
        text: str,
        web_app: WebAppInfo,
        type: str = 'web_app'
    ):
        self.type = type
        self.text = text
        self.web_app = web_app


class MenuButtonDefault(MenuButton):
    '''
    https://core.telegram.org/bots/api#menubuttondefault
    Describes that no specific value for the menu button was set.
    '''
    def __init__(
        self,
        type: str = 'default'
    ):
        self.type = type


class ResponseParameters(TelegramType):
    '''
    https://core.telegram.org/bots/api#responseparameters
    Describes why a request was unsuccessful.
    '''
    @classmethod
    def dese(cls, result):
        if result is None: return None
        obj = _check_dict(result)
        obj['migrate_to_chat_id'] = obj.get('migrate_to_chat_id')
        obj['retry_after'] = obj.get('retry_after')
        return cls(**obj)

    def __init__(
        self,
        migrate_to_chat_id: Optional[int] = None,
        retry_after: Optional[int] = None,
        **kwargs
    ):
        _get_kwargs(self, kwargs)
        self.migrate_to_chat_id = migrate_to_chat_id
        self.retry_after = retry_after


class InputMedia(TelegramType):
    '''
    https://core.telegram.org/bots/api#inputmedia
    This object represents the content of a media message to be sent. It should be one of
    - InputMediaAnimation
    - InputMediaDocument
    - InputMediaAudio
    - InputMediaPhoto
    - InputMediaVideo
    '''
    def __init__(
        self,
        **kwargs
    ):
        input_media = ', '.join([
            InputMediaPhoto.__name__,
            InputMediaVideo.__name__,
            InputMediaAnimation.__name__,
            InputMediaAudio.__name__,
            InputMediaDocument.__name__
        ])
        logger.warning(
            'InputMedia warning, expected one'
            f' of the following types: {input_media}.'
        )
        self.__dict__ = kwargs


class InputMediaPhoto(InputMedia):
    '''
    https://core.telegram.org/bots/api#inputmediaphoto
    Represents a photo to be sent.
    '''
    def __init__(
        self,
        media: str,
        caption: Optional[str] = None,
        parse_mode: Optional[str] = None,
        caption_entities: Optional[list[MessageEntity]] = None,
        has_spoiler: Optional[bool] = None,
        type: str = 'photo'
    ):
        self.type = type
        self.media = media
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.has_spoiler = has_spoiler


class InputMediaVideo(InputMedia):
    '''
    https://core.telegram.org/bots/api#inputmediavideo
    Represents a video to be sent.
    '''
    def __init__(
        self,
        media: str,
        thumbnail: Optional[Union[InputFile, str]] = None,
        caption: Optional[str] = None,
        parse_mode: Optional[str] = None,
        caption_entities: Optional[list[MessageEntity]] = None,
        width: Optional[int] = None,
        height: Optional[int] = None,
        duration: Optional[int] = None,
        supports_streaming: Optional[bool] = None,
        has_spoiler: Optional[bool] = None,
        type: str = 'video'
    ):
        self.type = type
        self.media = media
        self.thumbnail = thumbnail
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.width = width
        self.height = height
        self.duration = duration
        self.supports_streaming = supports_streaming
        self.has_spoiler = has_spoiler


class InputMediaAnimation(InputMedia):
    '''
    https://core.telegram.org/bots/api#inputmediaanimation
    Represents an animation file (GIF or H.264/MPEG-4 AVC video without sound) to be sent.
    '''
    def __init__(
        self,
        media: str,
        thumbnail: Optional[Union[InputFile, str]] = None,
        caption: Optional[str] = None,
        parse_mode: Optional[str] = None,
        caption_entities: Optional[list[MessageEntity]] = None,
        width: Optional[int] = None,
        height: Optional[int] = None,
        duration: Optional[int] = None,
        has_spoiler: Optional[bool] = None,
        type: str = 'animation'
    ):
        self.type = type
        self.media = media
        self.thumbnail = thumbnail
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.width = width
        self.height = height
        self.duration = duration
        self.has_spoiler = has_spoiler


class InputMediaAudio(InputMedia):
    '''
    https://core.telegram.org/bots/api#inputmediaaudio
    Represents an audio file to be treated as music to be sent.
    '''
    def __init__(
        self,
        media: str,
        thumbnail: Optional[Union[InputFile, str]] = None,
        caption: Optional[str] = None,
        parse_mode: Optional[str] = None,
        caption_entities: Optional[list[MessageEntity]] = None,
        duration: Optional[int] = None,
        performer: Optional[str] = None,
        title: Optional[str] = None,
        type: str = 'audio'
    ):
        self.type = type
        self.media = media
        self.thumbnail = thumbnail
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.duration = duration
        self.performer = performer
        self.title = title


class InputMediaDocument(InputMedia):
    '''
    https://core.telegram.org/bots/api#inputmediadocument
    Represents a general file to be sent.
    '''
    def __init__(
        self,
        media: str,
        thumbnail: Optional[Union[InputFile, str]] = None,
        caption: Optional[str] = None,
        parse_mode: Optional[str] = None,
        caption_entities: Optional[list[MessageEntity]] = None,
        disable_content_type_detection: Optional[bool] = None,
        type: str = 'document'
    ):
        self.type = type
        self.media = media
        self.thumbnail = thumbnail
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.disable_content_type_detection = disable_content_type_detection


class MaskPosition(TelegramType):
    '''
    https://core.telegram.org/bots/api#maskposition
    This object describes the position on faces where a mask should be placed by default.
    '''
    @classmethod
    def dese(cls, result):
        if result is None: return None
        obj = _check_dict(result)
        obj['point'] = obj.get('point')
        obj['x_shift'] = obj.get('x_shift')
        obj['y_shift'] = obj.get('y_shift')
        obj['scale'] = obj.get('scale')
        return cls(**obj)

    def __init__(
        self,
        point: str,
        x_shift: float,
        y_shift: float,
        scale: float
    ):
        self.point = point
        self.x_shift = x_shift
        self.y_shift = y_shift
        self.scale = scale


class Sticker(TelegramType):
    '''
    https://core.telegram.org/bots/api#sticker
    This object represents a sticker.
    '''
    @classmethod
    def dese(cls, result):
        if result is None: return None
        obj = _check_dict(result)
        obj['file_id'] = obj.get('file_id')
        obj['file_unique_id'] = obj.get('file_unique_id')
        obj['type'] = obj.get('type')
        obj['width'] = obj.get('width')
        obj['height'] = obj.get('height')
        obj['is_animated'] = obj.get('is_animated')
        obj['is_video'] = obj.get('is_video')
        obj['thumbnail'] = PhotoSize.dese(obj.get('thumbnail'))
        obj['emoji'] = obj.get('emoji')
        obj['set_name'] = obj.get('set_name')
        obj['premium_animation'] = File.dese(obj.get('premium_animation'))
        obj['mask_position'] = MaskPosition.dese(obj.get('mask_position'))
        obj['custom_emoji_id'] = obj.get('custom_emoji_id')
        obj['needs_repainting'] = obj.get('needs_repainting')
        obj['file_size'] = obj.get('file_size')
        return cls(**obj)

    def __init__(
        self,
        file_id: str,
        file_unique_id: str,
        type: str,
        width: int,
        height: int,
        is_animated: bool,
        is_video: bool,
        thumbnail: Optional[PhotoSize] = None,
        emoji: Optional[str] = None,
        set_name: Optional[str] = None,
        premium_animation: Optional[File] = None,
        mask_position: Optional[MaskPosition] = None,
        custom_emoji_id: Optional[str] = None,
        needs_repainting: Optional[Literal[True]] = None,
        file_size: Optional[int] = None,
        **kwargs
    ):
        _get_kwargs(self, kwargs)
        self.file_id = file_id
        self.file_unique_id = file_unique_id
        self.type = type
        self.width = width
        self.height = height
        self.is_animated = is_animated
        self.is_video = is_video
        self.thumbnail = thumbnail
        self.emoji = emoji
        self.set_name = set_name
        self.premium_animation = premium_animation
        self.mask_position = mask_position
        self.custom_emoji_id = custom_emoji_id
        self.needs_repainting = needs_repainting
        self.file_size = file_size


class StickerSet(TelegramType):
    '''
    https://core.telegram.org/bots/api#stickerset
    This object represents a sticker set.
    '''
    @classmethod
    def dese(cls, result):
        if result is None: return None
        obj = _check_dict(result)
        obj['name'] = obj.get('name')
        obj['title'] = obj.get('title')
        obj['sticker_type'] = obj.get('sticker_type')
        obj['is_animated'] = obj.get('is_animated')
        obj['is_video'] = obj.get('is_video')
        obj['stickers'] = [Sticker.dese(kwargs) for kwargs in obj.get('stickers')]
        obj['thumbnail'] = PhotoSize.dese(obj.get('thumbnail'))
        return cls(**obj)

    def __init__(
        self,
        name: str,
        title: str,
        sticker_type: str,
        is_animated: bool,
        is_video: bool,
        stickers: list[Sticker],
        thumbnail: Optional[PhotoSize] = None,
        **kwargs
    ):
        _get_kwargs(self, kwargs)
        self.name = name
        self.title = title
        self.sticker_type = sticker_type
        self.is_animated = is_animated
        self.is_video = is_video
        self.stickers = stickers
        self.thumbnail = thumbnail


class InputSticker(TelegramType):
    '''
    https://core.telegram.org/bots/api#inputsticker
    This object describes a sticker to be added to a sticker set.
    '''
    def __init__(
        self,
        sticker: Union[InputFile, str],
        emoji_list: list[str],
        mask_position: Optional[MaskPosition] = None,
        keywords: Optional[list[str]] = None
    ):
        self.sticker = sticker
        self.emoji_list = emoji_list
        self.mask_position = mask_position
        self.keywords = keywords


class InlineQuery(TelegramType):
    '''
    https://core.telegram.org/bots/api#inlinequery
    This object represents an incoming inline query. When the user sends
    an empty query, your bot could return some default or trending results.
    '''
    @classmethod
    def dese(cls, result):
        if result is None: return None
        obj = _check_dict(result)
        obj['id'] = obj.get('id')
        obj['from_user'] = User.dese(obj.get('from_user'))
        obj['query'] = obj.get('query')
        obj['offset'] = obj.get('offset')
        obj['chat_type'] = obj.get('chat_type')
        obj['location'] = Location.dese(obj.get('location'))
        return cls(**obj)

    def __init__(
        self,
        id: str,
        from_user: User,
        query: str,
        offset: str,
        chat_type: Optional[str] = None,
        location: Optional[Location] = None,
        **kwargs
    ):
        _get_kwargs(self, kwargs)
        self.id = id
        self.from_user = from_user
        self.query = query
        self.offset = offset
        self.chat_type = chat_type
        self.location = location


class InlineQueryResultsButton(TelegramType):
    '''
    https://core.telegram.org/bots/api#inlinequeryresultsbutton
    This object represents a button to be shown above inline query
    results. You must use exactly one of the optional fields.
    '''
    def __init__(
        self,
        text: str,
        web_app: Optional[WebAppInfo] = None,
        start_parameter: Optional[str] = None
    ):
        self.text = text
        self.web_app = web_app
        self.start_parameter = start_parameter


# InputMessageContent: 5 SUBCLASSES

class InputMessageContent(TelegramType):
    '''
    https://core.telegram.org/bots/api#inputmessagecontent
    This object represents the content of a message to be sent as a result of
    an inline query. Telegram clients currently support the following 5 types:
    - InputTextMessageContent
    - InputLocationMessageContent
    - InputVenueMessageContent
    - InputContactMessageContent
    - InputInvoiceMessageContent
    '''
    def __init__(
        self,
        **kwargs
    ):
        inputs = ', '.join([
            InputTextMessageContent.__name__,
            InputVenueMessageContent.__name__,
            InputLocationMessageContent.__name__,
            InputContactMessageContent.__name__,
            InputInvoiceMessageContent.__name__
        ])
        logger.warning(
            'InputMessageContent warning, expected'
            f' one of the following types: {inputs}.'
        )
        self.__dict__ = kwargs


class InputTextMessageContent(InputMessageContent):
    '''
    https://core.telegram.org/bots/api#inputtextmessagecontent
    Represents the content of a text message to be sent as the result of an inline query.
    '''
    def __init__(
        self,
        message_text: str,
        parse_mode: Optional[str] = None,
        entities: Optional[list[MessageEntity]] = None,
        link_preview_options: Optional[LinkPreviewOptions] = None
    ):
        self.message_text = message_text
        self.parse_mode = parse_mode
        self.entities = entities
        self.link_preview_options = link_preview_options


class InputLocationMessageContent(InputMessageContent):
    '''
    https://core.telegram.org/bots/api#inputlocationmessagecontent
    Represents the content of a location message to be sent as the result of an inline query.
    '''
    def __init__(
        self,
        latitude: float,
        longitude: float,
        horizontal_accuracy: Optional[float] = None,
        live_period: Optional[int] = None,
        heading: Optional[int] = None,
        proximity_alert_radius: Optional[int] = None
    ):
        self.latitude = latitude
        self.longitude = longitude
        self.horizontal_accuracy = horizontal_accuracy
        self.live_period = live_period
        self.heading = heading
        self.proximity_alert_radius = proximity_alert_radius


class InputVenueMessageContent(InputMessageContent):
    '''
    https://core.telegram.org/bots/api#inputvenuemessagecontent
    Represents the content of a venue message to be sent as the result of an inline query.
    '''
    def __init__(
        self,
        latitude: float,
        longitude: float,
        title: str,
        address: str,
        foursquare_id: Optional[str] = None,
        foursquare_type: Optional[str] = None,
        google_place_id: Optional[str] = None,
        google_place_type: Optional[str] = None
    ):
        self.latitude = latitude
        self.longitude = longitude
        self.title = title
        self.address = address
        self.foursquare_id = foursquare_id
        self.foursquare_type = foursquare_type
        self.google_place_id = google_place_id
        self.google_place_type = google_place_type


class InputContactMessageContent(InputMessageContent):
    '''
    https://core.telegram.org/bots/api#inputcontactmessagecontent
    Represents the content of a contact message to be sent as the result of an inline query.
    '''
    def __init__(
        self,
        phone_number: str,
        first_name: str,
        last_name: Optional[str] = None,
        vcard: Optional[str] = None
    ):
        self.phone_number = phone_number
        self.first_name = first_name
        self.last_name = last_name
        self.vcard = vcard


class InputInvoiceMessageContent(InputMessageContent):
    '''
    https://core.telegram.org/bots/api#inputinvoicemessagecontent
    Represents the content of an invoice message to be sent as the result of an inline query.
    '''
    def __init__(
        self,
        title: str,
        description: str,
        payload: str,
        provider_token: str,
        currency: str,
        prices: list[LabeledPrice],
        max_tip_amount: Optional[int] = None,
        suggested_tip_amounts: Optional[list[int]] = None,
        provider_data: Optional[str] = None,
        photo_url: Optional[str] = None,
        photo_size: Optional[int] = None,
        photo_width: Optional[int] = None,
        photo_height: Optional[int] = None,
        need_name: Optional[bool] = None,
        need_phone_number: Optional[bool] = None,
        need_email: Optional[bool] = None,
        need_shipping_address: Optional[bool] = None,
        send_phone_number_to_provider: Optional[bool] = None,
        send_email_to_provider: Optional[bool] = None,
        is_flexible: Optional[bool] = None
    ):
        self.title = title
        self.description = description
        self.payload = payload
        self.provider_token = provider_token
        self.currency = currency
        self.prices = prices
        self.max_tip_amount = max_tip_amount
        self.suggested_tip_amounts = suggested_tip_amounts
        self.provider_data = provider_data
        self.photo_url = photo_url
        self.photo_size = photo_size
        self.photo_width = photo_width
        self.photo_height = photo_height
        self.need_name = need_name
        self.need_phone_number = need_phone_number
        self.need_email = need_email
        self.need_shipping_address = need_shipping_address
        self.send_phone_number_to_provider = send_phone_number_to_provider
        self.send_email_to_provider = send_email_to_provider
        self.is_flexible = is_flexible


# InlineQueryResult: 20 SUBCLASSES


class InlineQueryResult(TelegramType):
    '''
    https://core.telegram.org/bots/api#inlinequeryresult
    This object represents one result of an inline query. Telegram
    clients currently support results of the following 20 types:
    - InlineQueryResultCachedAudio
    - InlineQueryResultCachedDocument
    - InlineQueryResultCachedGif
    - InlineQueryResultCachedMpeg4Gif
    - InlineQueryResultCachedPhoto
    - InlineQueryResultCachedSticker
    - InlineQueryResultCachedVideo
    - InlineQueryResultCachedVoice
    - InlineQueryResultArticle
    - InlineQueryResultAudio
    - InlineQueryResultContact
    - InlineQueryResultGame
    - InlineQueryResultDocument
    - InlineQueryResultGif
    - InlineQueryResultLocation
    - InlineQueryResultMpeg4Gif
    - InlineQueryResultPhoto
    - InlineQueryResultVenue
    - InlineQueryResultVideo
    - InlineQueryResultVoice
    '''
    def __init__(
        self,
        **kwargs
    ):
        inline_query_results = ', '.join([
            InlineQueryResultArticle.__name__,
            InlineQueryResultPhoto.__name__,
            InlineQueryResultGif.__name__,
            InlineQueryResultMpeg4Gif.__name__,
            InlineQueryResultVideo.__name__,
            InlineQueryResultAudio.__name__,
            InlineQueryResultVoice.__name__,
            InlineQueryResultDocument.__name__,
            InlineQueryResultLocation.__name__,
            InlineQueryResultVenue.__name__,
            InlineQueryResultContact.__name__,
            InlineQueryResultGame.__name__,
            InlineQueryResultCachedPhoto.__name__,
            InlineQueryResultCachedGif.__name__,
            InlineQueryResultCachedMpeg4Gif.__name__,
            InlineQueryResultCachedSticker.__name__,
            InlineQueryResultCachedDocument.__name__,
            InlineQueryResultCachedVideo.__name__,
            InlineQueryResultCachedVoice.__name__,
            InlineQueryResultCachedAudio.__name__
        ])
        logger.warning(
            'InlineQueryResult warning, expected one of'
            f' the following types: {inline_query_results}.'
        )
        self.__dict__ = kwargs


class InlineQueryResultArticle(InlineQueryResult):
    '''
    https://core.telegram.org/bots/api#inlinequeryresultarticle
    Represents a link to an article or web page.
    '''
    def __init__(
        self,
        id: str,
        title: str,
        input_message_content: InputMessageContent,
        reply_markup: Optional[InlineKeyboardMarkup] = None,
        url: Optional[str] = None,
        hide_url: Optional[bool] = None,
        description: Optional[str] = None,
        thumbnail_url: Optional[str] = None,
        thumbnail_width: Optional[int] = None,
        thumbnail_height: Optional[int] = None,
        type: str = 'article'
    ):
        self.type = type
        self.id = id
        self.title = title
        self.input_message_content = input_message_content
        self.reply_markup = reply_markup
        self.url = url
        self.hide_url = hide_url
        self.description = description
        self.thumbnail_url = thumbnail_url
        self.thumbnail_width = thumbnail_width
        self.thumbnail_height = thumbnail_height


class InlineQueryResultPhoto(InlineQueryResult):
    '''
    https://core.telegram.org/bots/api#inlinequeryresultphoto
    Represents a link to a photo. By default, this photo will be sent by the user with optional caption.
    Alternatively, you can use input_message_content to send a message with the specified content instead of the photo.
    '''
    def __init__(
        self,
        id: str,
        photo_url: str,
        thumbnail_url: str,
        photo_width: Optional[int] = None,
        photo_height: Optional[int] = None,
        title: Optional[str] = None,
        description: Optional[str] = None,
        caption: Optional[str] = None,
        parse_mode: Optional[str] = None,
        caption_entities: Optional[list[MessageEntity]] = None,
        reply_markup: Optional[InlineKeyboardMarkup] = None,
        input_message_content: Optional[InputMessageContent] = None,
        type: str = 'photo'
    ):
        self.type = type
        self.id = id
        self.photo_url = photo_url
        self.thumbnail_url = thumbnail_url
        self.photo_width = photo_width
        self.photo_height = photo_height
        self.title = title
        self.description = description
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content


class InlineQueryResultGif(InlineQueryResult):
    '''
    https://core.telegram.org/bots/api#inlinequeryresultgif
    Represents a link to an animated GIF file. By default, this animated GIF file will be sent by the user with optional
    caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the animation.
    '''
    def __init__(
        self,
        id: str,
        gif_url: str,
        thumbnail_url: str,
        gif_width: Optional[int] = None,
        gif_height: Optional[int] = None,
        gif_duration: Optional[int] = None,
        thumbnail_mime_type: Optional[str] = None,
        title: Optional[str] = None,
        caption: Optional[str] = None,
        parse_mode: Optional[str] = None,
        caption_entities: Optional[list[MessageEntity]] = None,
        reply_markup: Optional[InlineKeyboardMarkup] = None,
        input_message_content: Optional[InputMessageContent] = None,
        type: str = 'gif'
    ):
        self.type = type
        self.id = id
        self.gif_url = gif_url
        self.thumbnail_url = thumbnail_url
        self.gif_width = gif_width
        self.gif_height = gif_height
        self.gif_duration = gif_duration
        self.thumbnail_mime_type = thumbnail_mime_type
        self.title = title
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content


class InlineQueryResultMpeg4Gif(InlineQueryResult):
    '''
    https://core.telegram.org/bots/api#inlinequeryresultmpeg4gif
    Represents a link to a video animation (H.264/MPEG-4 AVC video without sound). By default,
    this animated MPEG-4 file will be sent by the user with optional caption. Alternatively, you can
    use input_message_content to send a message with the specified content instead of the animation.
    '''
    def __init__(
        self,
        id: str,
        mpeg4_url: str,
        thumbnail_url: str,
        mpeg4_width: Optional[int] = None,
        mpeg4_height: Optional[int] = None,
        mpeg4_duration: Optional[int] = None,
        thumbnail_mime_type: Optional[str] = None,
        title: Optional[str] = None,
        caption: Optional[str] = None,
        parse_mode: Optional[str] = None,
        caption_entities: Optional[list[MessageEntity]] = None,
        reply_markup: Optional[InlineKeyboardMarkup] = None,
        input_message_content: Optional[InputMessageContent] = None,
        type: str = 'mpeg4_gif'
    ):
        self.type = type
        self.id = id
        self.mpeg4_url = mpeg4_url
        self.thumbnail_url = thumbnail_url
        self.mpeg4_width = mpeg4_width
        self.mpeg4_height = mpeg4_height
        self.mpeg4_duration = mpeg4_duration
        self.thumbnail_mime_type = thumbnail_mime_type
        self.title = title
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content


class InlineQueryResultVideo(InlineQueryResult):
    '''
    https://core.telegram.org/bots/api#inlinequeryresultvideo
    Represents a link to a page containing an embedded video player or a video file. By
    default, this video file will be sent by the user with an optional caption. Alternatively, you
    can use input_message_content to send a message with the specified content instead of the video.
    '''
    def __init__(
        self,
        id: str,
        video_url: str,
        mime_type: str,
        thumbnail_url: str,
        title: str,
        caption: Optional[str] = None,
        parse_mode: Optional[str] = None,
        caption_entities: Optional[list[MessageEntity]] = None,
        video_width: Optional[int] = None,
        video_height: Optional[int] = None,
        video_duration: Optional[int] = None,
        description: Optional[str] = None,
        reply_markup: Optional[InlineKeyboardMarkup] = None,
        input_message_content: Optional[InputMessageContent] = None,
        type: str = 'video'
    ):
        self.type = type
        self.id = id
        self.video_url = video_url
        self.mime_type = mime_type
        self.thumbnail_url = thumbnail_url
        self.title = title
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.video_width = video_width
        self.video_height = video_height
        self.video_duration = video_duration
        self.description = description
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content


class InlineQueryResultAudio(InlineQueryResult):
    '''
    https://core.telegram.org/bots/api#inlinequeryresultaudio
    Represents a link to an MP3 audio file. By default, this audio file will be sent by the user.
    Alternatively, you can use input_message_content to send a message with the specified content instead of the audio.
    '''
    def __init__(
        self,
        id: str,
        audio_url: str,
        title: str,
        caption: Optional[str] = None,
        parse_mode: Optional[str] = None,
        caption_entities: Optional[list[MessageEntity]] = None,
        performer: Optional[str] = None,
        audio_duration: Optional[int] = None,
        reply_markup: Optional[InlineKeyboardMarkup] = None,
        input_message_content: Optional[InputMessageContent] = None,
        type: str = 'audio'
    ):
        self.type = type
        self.id = id
        self.audio_url = audio_url
        self.title = title
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.performer = performer
        self.audio_duration = audio_duration
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content


class InlineQueryResultVoice(InlineQueryResult):
    '''
    https://core.telegram.org/bots/api#inlinequeryresultvoice
    Represents a link to a voice recording in an .OGG container encoded with OPUS.
    By default, this voice recording will be sent by the user. Alternatively, you can use
    input_message_content to send a message with the specified content instead of the the voice message.
    '''
    def __init__(
        self,
        id: str,
        voice_url: str,
        title: str,
        caption: Optional[str] = None,
        parse_mode: Optional[str] = None,
        caption_entities: Optional[list[MessageEntity]] = None,
        voice_duration: Optional[int] = None,
        reply_markup: Optional[InlineKeyboardMarkup] = None,
        input_message_content: Optional[InputMessageContent] = None,
        type: str = 'voice'
    ):
        self.type = type
        self.id = id
        self.voice_url = voice_url
        self.title = title
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.voice_duration = voice_duration
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content


class InlineQueryResultDocument(InlineQueryResult):
    '''
    https://core.telegram.org/bots/api#inlinequeryresultdocument
    Represents a link to a file. By default, this file will be sent by the user with an optional
    caption. Alternatively, you can use input_message_content to send a message with the specified
    content instead of the file. Currently, only .PDF and .ZIP files can be sent using this method.
    '''
    def __init__(
        self,
        id: str,
        title: str,
        document_url: str,
        mime_type: str,
        caption: Optional[str] = None,
        parse_mode: Optional[str] = None,
        caption_entities: Optional[list[MessageEntity]] = None,
        description: Optional[str] = None,
        reply_markup: Optional[InlineKeyboardMarkup] = None,
        input_message_content: Optional[InputMessageContent] = None,
        thumbnail_url: Optional[str] = None,
        thumbnail_width: Optional[int] = None,
        thumbnail_height: Optional[int] = None,
        type: str = 'document'
    ):
        self.type = type
        self.id = id
        self.title = title
        self.document_url = document_url
        self.mime_type = mime_type
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.description = description
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content
        self.thumbnail_url = thumbnail_url
        self.thumbnail_width = thumbnail_width
        self.thumbnail_height = thumbnail_height


class InlineQueryResultLocation(InlineQueryResult):
    '''
    https://core.telegram.org/bots/api#inlinequeryresultlocation
    Represents a location on a map. By default, the location will be sent by the user. Alternatively,
    you can use input_message_content to send a message with the specified content instead of the location.
    '''
    def __init__(
        self,
        id: str,
        latitude: float,
        longitude: float,
        title: str,
        horizontal_accuracy: Optional[float] = None,
        live_period: Optional[int] = None,
        heading: Optional[int] = None,
        proximity_alert_radius: Optional[int] = None,
        reply_markup: Optional[InlineKeyboardMarkup] = None,
        input_message_content: Optional[InputMessageContent] = None,
        thumbnail_url: Optional[str] = None,
        thumbnail_width: Optional[int] = None,
        thumbnail_height: Optional[int] = None,
        type: str = 'location'
    ):
        self.type = type
        self.id = id
        self.latitude = latitude
        self.longitude = longitude
        self.title = title
        self.horizontal_accuracy = horizontal_accuracy
        self.live_period = live_period
        self.heading = heading
        self.proximity_alert_radius = proximity_alert_radius
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content
        self.thumbnail_url = thumbnail_url
        self.thumbnail_width = thumbnail_width
        self.thumbnail_height = thumbnail_height


class InlineQueryResultVenue(InlineQueryResult):
    '''
    https://core.telegram.org/bots/api#inlinequeryresultvenue
    Represents a venue. By default, the venue will be sent by the user. Alternatively, you can
    use input_message_content to send a message with the specified content instead of the venue.
    '''
    def __init__(
        self,
        id: str,
        latitude: float,
        longitude: float,
        title: str,
        address: str,
        foursquare_id: Optional[str] = None,
        foursquare_type: Optional[str] = None,
        google_place_id: Optional[str] = None,
        google_place_type: Optional[str] = None,
        reply_markup: Optional[InlineKeyboardMarkup] = None,
        input_message_content: Optional[InputMessageContent] = None,
        thumbnail_url: Optional[str] = None,
        thumbnail_width: Optional[int] = None,
        thumbnail_height: Optional[int] = None,
        type: str = 'venue'
    ):
        self.type = type
        self.id = id
        self.latitude = latitude
        self.longitude = longitude
        self.title = title
        self.address = address
        self.foursquare_id = foursquare_id
        self.foursquare_type = foursquare_type
        self.google_place_id = google_place_id
        self.google_place_type = google_place_type
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content
        self.thumbnail_url = thumbnail_url
        self.thumbnail_width = thumbnail_width
        self.thumbnail_height = thumbnail_height


class InlineQueryResultContact(InlineQueryResult):
    '''
    https://core.telegram.org/bots/api#inlinequeryresultcontact
    Represents a contact with a phone number. By default, this contact will be sent by the user. Alternatively,
    you can use input_message_content to send a message with the specified content instead of the contact.
    '''
    def __init__(
        self,
        id: str,
        phone_number: str,
        first_name: str,
        last_name: Optional[str] = None,
        vcard: Optional[str] = None,
        reply_markup: Optional[InlineKeyboardMarkup] = None,
        input_message_content: Optional[InputMessageContent] = None,
        thumbnail_url: Optional[str] = None,
        thumbnail_width: Optional[int] = None,
        thumbnail_height: Optional[int] = None,
        type: str = 'contact'
    ):
        self.type = type
        self.id = id
        self.phone_number = phone_number
        self.first_name = first_name
        self.last_name = last_name
        self.vcard = vcard
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content
        self.thumbnail_url = thumbnail_url
        self.thumbnail_width = thumbnail_width
        self.thumbnail_height = thumbnail_height


class InlineQueryResultGame(InlineQueryResult):
    '''
    https://core.telegram.org/bots/api#inlinequeryresultgame
    Represents a Game.
    '''
    def __init__(
        self,
        id: str,
        game_short_name: str,
        reply_markup: Optional[InlineKeyboardMarkup] = None,
        type: str = 'game'
    ):
        self.type = type
        self.id = id
        self.game_short_name = game_short_name
        self.reply_markup = reply_markup


class InlineQueryResultCachedPhoto(InlineQueryResult):
    '''
    https://core.telegram.org/bots/api#inlinequeryresultcachedphoto
    Represents a link to a photo stored on the Telegram servers. By default, this
    photo will be sent by the user with an optional caption. Alternatively, you can use
    input_message_content to send a message with the specified content instead of the photo.
    '''
    def __init__(
        self,
        id: str,
        photo_file_id: str,
        title: Optional[str] = None,
        description: Optional[str] = None,
        caption: Optional[str] = None,
        parse_mode: Optional[str] = None,
        caption_entities: Optional[list[MessageEntity]] = None,
        reply_markup: Optional[InlineKeyboardMarkup] = None,
        input_message_content: Optional[InputMessageContent] = None,
        type: str = 'photo'
    ):
        self.type = type
        self.id = id
        self.photo_file_id = photo_file_id
        self.title = title
        self.description = description
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content


class InlineQueryResultCachedGif(InlineQueryResult):
    '''
    https://core.telegram.org/bots/api#inlinequeryresultcachedgif
    Represents a link to an animated GIF file stored on the Telegram servers. By default,
    this animated GIF file will be sent by the user with an optional caption. Alternatively, you
    can use input_message_content to send a message with specified content instead of the animation.
    '''
    def __init__(
        self,
        id: str,
        gif_file_id: str,
        title: Optional[str] = None,
        caption: Optional[str] = None,
        parse_mode: Optional[str] = None,
        caption_entities: Optional[list[MessageEntity]] = None,
        reply_markup: Optional[InlineKeyboardMarkup] = None,
        input_message_content: Optional[InputMessageContent] = None,
        type: str = 'gif'
    ):
        self.type = type
        self.id = id
        self.gif_file_id = gif_file_id
        self.title = title
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content


class InlineQueryResultCachedMpeg4Gif(InlineQueryResult):
    '''
    https://core.telegram.org/bots/api#inlinequeryresultcachedmpeg4gif
    Represents a link to a video animation (H.264/MPEG-4 AVC video without sound) stored on the Telegram servers.
    By default, this animated MPEG-4 file will be sent by the user with an optional caption. Alternatively, you
    can use input_message_content to send a message with the specified content instead of the animation.
    '''
    def __init__(
        self,
        id: str,
        mpeg4_file_id: str,
        title: Optional[str] = None,
        caption: Optional[str] = None,
        parse_mode: Optional[str] = None,
        caption_entities: Optional[list[MessageEntity]] = None,
        reply_markup: Optional[InlineKeyboardMarkup] = None,
        input_message_content: Optional[InputMessageContent] = None,
        type: str = 'mpeg4_gif'
    ):
        self.type = type
        self.id = id
        self.mpeg4_file_id = mpeg4_file_id
        self.title = title
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content


class InlineQueryResultCachedSticker(InlineQueryResult):
    '''
    https://core.telegram.org/bots/api#inlinequeryresultcachedsticker
    Represents a link to a sticker stored on the Telegram servers.
    By default, this sticker will be sent by the user. Alternatively, you can use
    input_message_content to send a message with the specified content instead of the sticker.
    '''
    def __init__(
        self,
        id: str,
        sticker_file_id: str,
        reply_markup: Optional[InlineKeyboardMarkup] = None,
        input_message_content: Optional[InputMessageContent] = None,
        type: str = 'sticker'
    ):
        self.type = type
        self.id = id
        self.sticker_file_id = sticker_file_id
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content


class InlineQueryResultCachedDocument(InlineQueryResult):
    '''
    https://core.telegram.org/bots/api#inlinequeryresultcacheddocument
    Represents a link to a file stored on the Telegram servers. By default, this
    file will be sent by the user with an optional caption. Alternatively, you can use
    input_message_content to send a message with the specified content instead of the file.
    '''
    def __init__(
        self,
        id: str,
        title: str,
        document_file_id: str,
        description: Optional[str] = None,
        caption: Optional[str] = None,
        parse_mode: Optional[str] = None,
        caption_entities: Optional[list[MessageEntity]] = None,
        reply_markup: Optional[InlineKeyboardMarkup] = None,
        input_message_content: Optional[InputMessageContent] = None,
        type: str = 'document'
    ):
        self.type = type
        self.id = id
        self.title = title
        self.document_file_id = document_file_id
        self.description = description
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content


class InlineQueryResultCachedVideo(InlineQueryResult):
    '''
    https://core.telegram.org/bots/api#inlinequeryresultcachedvideo
    Represents a link to a video file stored on the Telegram servers. By default, this
    video file will be sent by the user with an optional caption. Alternatively, you can
    use input_message_content to send a message with the specified content instead of the video.
    '''
    def __init__(
        self,
        id: str,
        video_file_id: str,
        title: str,
        description: Optional[str] = None,
        caption: Optional[str] = None,
        parse_mode: Optional[str] = None,
        caption_entities: Optional[list[MessageEntity]] = None,
        reply_markup: Optional[InlineKeyboardMarkup] = None,
        input_message_content: Optional[InputMessageContent] = None,
        type: str = 'video'
    ):
        self.type = type
        self.id = id
        self.video_file_id = video_file_id
        self.title = title
        self.description = description
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content


class InlineQueryResultCachedVoice(InlineQueryResult):
    '''
    https://core.telegram.org/bots/api#inlinequeryresultcachedvoice
    Represents a link to a voice message stored on the Telegram servers.
    By default, this voice message will be sent by the user. Alternatively, you can use
    input_message_content to send a message with the specified content instead of the voice message.
    '''
    def __init__(
        self,
        id: str,
        voice_file_id: str,
        title: str,
        caption: Optional[str] = None,
        parse_mode: Optional[str] = None,
        caption_entities: Optional[list[MessageEntity]] = None,
        reply_markup: Optional[InlineKeyboardMarkup] = None,
        input_message_content: Optional[InputMessageContent] = None,
        type: str = 'voice'
    ):
        self.type = type
        self.id = id
        self.voice_file_id = voice_file_id
        self.title = title
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content


class InlineQueryResultCachedAudio(InlineQueryResult):
    '''
    https://core.telegram.org/bots/api#inlinequeryresultcachedaudio
    Represents a link to an MP3 audio file stored on the Telegram servers.
    By default, this audio file will be sent by the user. Alternatively, you can use
    input_message_content to send a message with the specified content instead of the audio.
    '''
    def __init__(
        self,
        id: str,
        audio_file_id: str,
        caption: Optional[str] = None,
        parse_mode: Optional[str] = None,
        caption_entities: Optional[list[MessageEntity]] = None,
        reply_markup: Optional[InlineKeyboardMarkup] = None,
        input_message_content: Optional[InputMessageContent] = None,
        type: str = 'audio'
    ):
        self.type = type
        self.id = id
        self.audio_file_id = audio_file_id
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content


class ChosenInlineResult(TelegramType):
    '''
    https://core.telegram.org/bots/api#choseninlineresult
    Represents a result of an inline query that was chosen by the user and sent to their chat partner.
    '''
    @classmethod
    def dese(cls, result):
        if result is None: return None
        obj = _check_dict(result)
        obj['result_id'] = obj.get('result_id')
        obj['from_user'] = User.dese(obj.get('from_user'))
        obj['location'] = Location.dese(obj.get('location'))
        obj['inline_message_id'] = obj.get('inline_message_id')
        obj['query'] = obj.get('query')
        return cls(**obj)

    def __init__(
        self,
        result_id: str,
        from_user: User,
        query: str,
        location: Optional[Location] = None,
        inline_message_id: Optional[str] = None,
        **kwargs
    ):
        _get_kwargs(self, kwargs)
        self.result_id = result_id
        self.from_user = from_user
        self.query = query
        self.location = location
        self.inline_message_id = inline_message_id


class SentWebAppMessage(TelegramType):
    '''
    https://core.telegram.org/bots/api#sentwebappmessage
    Describes an inline message sent by a Web App on behalf of a user.
    '''
    @classmethod
    def dese(cls, result):
        if result is None: return None
        obj = _check_dict(result)
        obj['inline_message_id'] = obj.get('inline_message_id')
        return cls(**obj)

    def __init__(
        self,
        inline_message_id: Optional[str] = None,
        **kwargs
    ):
        _get_kwargs(self, kwargs)
        self.inline_message_id = inline_message_id


class Invoice(TelegramType):
    '''
    https://core.telegram.org/bots/api#invoice
    This object contains basic information about an invoice.
    '''
    @classmethod
    def dese(cls, result):
        if result is None: return None
        obj = _check_dict(result)
        obj['title'] = obj.get('title')
        obj['description'] = obj.get('description')
        obj['start_parameter'] = obj.get('start_parameter')
        obj['currency'] = obj.get('currency')
        obj['total_amount'] = obj.get('total_amount')
        return cls(**obj)

    def __init__(
        self,
        title: str,
        description: str,
        start_parameter: str,
        currency: str,
        total_amount: int,
        **kwargs
    ):
        _get_kwargs(self, kwargs)
        self.title = title
        self.description = description
        self.start_parameter = start_parameter
        self.currency = currency
        self.total_amount = total_amount


class ShippingAddress(TelegramType):
    '''
    https://core.telegram.org/bots/api#shippingaddress
    This object represents a shipping address.
    '''
    @classmethod
    def dese(cls, result):
        if result is None: return None
        obj = _check_dict(result)
        obj['country_code'] = obj.get('country_code')
        obj['state'] = obj.get('state')
        obj['city'] = obj.get('city')
        obj['street_line1'] = obj.get('street_line1')
        obj['street_line2'] = obj.get('street_line2')
        obj['post_code'] = obj.get('post_code')
        return cls(**obj)

    def __init__(
        self,
        country_code: str,
        state: str,
        city: str,
        street_line1: str,
        street_line2: str,
        post_code: str,
        **kwargs
    ):
        _get_kwargs(self, kwargs)
        self.country_code = country_code
        self.state = state
        self.city = city
        self.street_line1 = street_line1
        self.street_line2 = street_line2
        self.post_code = post_code


class OrderInfo(TelegramType):
    '''
    https://core.telegram.org/bots/api#orderinfo
    This object represents information about an order.
    '''
    @classmethod
    def dese(cls, result):
        if result is None: return None
        obj = _check_dict(result)
        obj['name'] = obj.get('name')
        obj['phone_number'] = obj.get('phone_number')
        obj['email'] = obj.get('email')
        obj['shipping_address'] = ShippingAddress.dese(obj.get('shipping_address'))
        return cls(**obj)

    def __init__(
        self,
        name: Optional[str] = None,
        phone_number: Optional[str] = None,
        email: Optional[str] = None,
        shipping_address: Optional[ShippingAddress] = None,
        **kwargs
    ):
        _get_kwargs(self, kwargs)
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.shipping_address = shipping_address


class ShippingOption(TelegramType):
    '''
    https://core.telegram.org/bots/api#shippingoption
    This object represents one shipping option.
    '''
    def __init__(
        self,
        id: str,
        title: str,
        prices: list[LabeledPrice]
    ):
        self.id = id
        self.title = title
        self.prices = prices


class SuccessfulPayment(TelegramType):
    '''
    https://core.telegram.org/bots/api#successfulpayment
    This object contains basic information about a successful payment.
    '''
    @classmethod
    def dese(cls, result):
        if result is None: return None
        obj = _check_dict(result)
        obj['currency'] = obj.get('currency')
        obj['total_amount'] = obj.get('total_amount')
        obj['invoice_payload'] = obj.get('invoice_payload')
        obj['shipping_option_id'] = obj.get('shipping_option_id')
        obj['order_info'] = OrderInfo.dese(obj.get('order_info'))
        obj['telegram_payment_charge_id'] = obj.get('telegram_payment_charge_id')
        obj['provider_payment_charge_id'] = obj.get('provider_payment_charge_id')
        return cls(**obj)

    def __init__(
        self,
        currency: str,
        total_amount: int,
        invoice_payload: str,
        telegram_payment_charge_id: str,
        provider_payment_charge_id: str,
        shipping_option_id: Optional[str] = None,
        order_info: Optional[OrderInfo] = None,
        **kwargs
    ):
        _get_kwargs(self, kwargs)
        self.currency = currency
        self.total_amount = total_amount
        self.invoice_payload = invoice_payload
        self.telegram_payment_charge_id = telegram_payment_charge_id
        self.provider_payment_charge_id = provider_payment_charge_id
        self.shipping_option_id = shipping_option_id
        self.order_info = order_info


class ShippingQuery(TelegramType):
    '''
    https://core.telegram.org/bots/api#shippingquery
    This object contains information about an incoming shipping query.
    '''
    @classmethod
    def dese(cls, result):
        if result is None: return None
        obj = _check_dict(result)
        obj['id'] = obj.get('id')
        obj['from_user'] = User.dese(obj.get('from_user'))
        obj['invoice_payload'] = obj.get('invoice_payload')
        obj['shipping_address'] = ShippingAddress.dese(obj.get('shipping_address'))
        return cls(**obj)

    def __init__(
        self,
        id: str,
        from_user: User,
        invoice_payload: str,
        shipping_address: ShippingAddress,
        **kwargs
    ):
        _get_kwargs(self, kwargs)
        self.id = id
        self.from_user = from_user
        self.invoice_payload = invoice_payload
        self.shipping_address = shipping_address


class PreCheckoutQuery(TelegramType):
    '''
    https://core.telegram.org/bots/api#precheckoutquery
    This object contains information about an incoming pre-checkout query.
    '''
    @classmethod
    def dese(cls, result):
        if result is None: return None
        obj = _check_dict(result)
        obj['id'] = obj.get('id')
        obj['from_user'] = User.dese(obj.get('from_user'))
        obj['currency'] = obj.get('currency')
        obj['total_amount'] = obj.get('total_amount')
        obj['invoice_payload'] = obj.get('invoice_payload')
        obj['shipping_option_id'] = obj.get('shipping_option_id')
        obj['order_info'] = OrderInfo.dese(obj.get('order_info'))
        return cls(**obj)

    def __init__(
        self,
        id: str,
        from_user: User,
        currency: str,
        total_amount: int,
        invoice_payload: str,
        shipping_option_id: Optional[str] = None,
        order_info: Optional[OrderInfo] = None,
        **kwargs
    ):
        _get_kwargs(self, kwargs)
        self.id = id
        self.from_user = from_user
        self.currency = currency
        self.total_amount = total_amount
        self.invoice_payload = invoice_payload
        self.shipping_option_id = shipping_option_id
        self.order_info = order_info


class PassportFile(TelegramType):
    '''
    https://core.telegram.org/bots/api#passportfile
    This object represents a file uploaded to Telegram Passport. Currently all
    Telegram Passport files are in JPEG format when decrypted and don't exceed 10MB.
    '''
    @classmethod
    def dese(cls, result):
        if result is None: return None
        obj = _check_dict(result)
        obj['file_id'] = obj.get('file_id')
        obj['file_unique_id'] = obj.get('file_unique_id')
        obj['file_size'] = obj.get('file_size')
        obj['file_date'] = obj.get('file_date')
        return cls(**obj)

    def __init__(
        self,
        file_id: str,
        file_unique_id: str,
        file_size: int,
        file_date: int,
        **kwargs
    ):
        _get_kwargs(self, kwargs)
        self.file_id = file_id
        self.file_unique_id = file_unique_id
        self.file_size = file_size
        self.file_date = file_date


class EncryptedPassportElement(TelegramType):
    '''
    https://core.telegram.org/bots/api#encryptedpassportelement
    Describes documents or other Telegram Passport elements shared with the bot by the user.
    '''
    @classmethod
    def dese(cls, result):
        if result is None: return None
        obj = _check_dict(result)
        obj['type'] = obj.get('type')
        obj['hash'] = obj.get('hash')
        obj['data'] = obj.get('data')
        obj['phone_number'] = obj.get('phone_number')
        obj['email'] = obj.get('email')
        obj['files'] = [PassportFile.dese(kwargs) for kwargs in obj.get('files')] if 'files' in obj else None
        obj['front_side'] = PassportFile.dese(obj.get('front_side'))
        obj['reverse_side'] = PassportFile.dese(obj.get('reverse_side'))
        obj['selfie'] = PassportFile.dese(obj.get('selfie'))
        obj['translation'] = [PassportFile.dese(kwargs) for kwargs in obj.get('translation')] if 'translation' in obj else None
        return cls(**obj)

    def __init__(
        self,
        type: str,
        hash: str,
        data: Optional[str] = None,
        phone_number: Optional[str] = None,
        email: Optional[str] = None,
        files: Optional[list[PassportFile]] = None,
        front_side: Optional[PassportFile] = None,
        reverse_side: Optional[PassportFile] = None,
        selfie: Optional[PassportFile] = None,
        translation: Optional[list[PassportFile]] = None,
        **kwargs
    ):
        _get_kwargs(self, kwargs)
        self.type = type
        self.hash = hash
        self.data = data
        self.phone_number = phone_number
        self.email = email
        self.files = files
        self.front_side = front_side
        self.reverse_side = reverse_side
        self.selfie = selfie
        self.translation = translation


class EncryptedCredentials(TelegramType):
    '''
    https://core.telegram.org/bots/api#encryptedcredentials
    Describes data required for decrypting and authenticating EncryptedPassportElement. See the Telegram
    Passport Documentation for a complete description of the data decryption and authentication processes.
    '''
    @classmethod
    def dese(cls, result):
        if result is None: return None
        obj = _check_dict(result)
        obj['data'] = obj.get('data')
        obj['hash'] = obj.get('hash')
        obj['secret'] = obj.get('secret')
        return cls(**obj)

    def __init__(
        self,
        data: str,
        hash: str,
        secret: str,
        **kwargs
    ):
        _get_kwargs(self, kwargs)
        self.data = data
        self.hash = hash
        self.secret = secret


class PassportData(TelegramType):
    '''
    https://core.telegram.org/bots/api#passportdata
    Describes Telegram Passport data shared with the bot by the user.
    '''
    @classmethod
    def dese(cls, result):
        if result is None: return None
        obj = _check_dict(result)
        obj['data'] = [EncryptedPassportElement.dese(kwargs) for kwargs in obj.get('data')]
        obj['credentials'] = EncryptedCredentials.dese(obj.get('credentials'))
        return cls(**obj)

    def __init__(
        self,
        data: list[EncryptedPassportElement],
        credentials: EncryptedCredentials,
        **kwargs
    ):
        _get_kwargs(self, kwargs)
        self.data = data
        self.credentials = credentials


# PassportElementError: 5 SUBCLASSES

class PassportElementError(TelegramType):
    '''
    https://core.telegram.org/bots/api#passportelementerror
    This object represents an error in the Telegram Passport element which
    was submitted that should be resolved by the user. It should be one of:
    - PassportElementErrorDataField
    - PassportElementErrorFrontSide
    - PassportElementErrorReverseSide
    - PassportElementErrorSelfie
    - PassportElementErrorFile
    - PassportElementErrorFiles
    - PassportElementErrorTranslationFile
    - PassportElementErrorTranslationFiles
    - PassportElementErrorUnspecified
    '''
    def __init__(
        self,
        **kwargs
    ):
        errors = ', '.join([
            PassportElementErrorDataField.__name__,
            PassportElementErrorFrontSide.__name__,
            PassportElementErrorReverseSide.__name__,
            PassportElementErrorSelfie.__name__,
            PassportElementErrorFile.__name__,
            PassportElementErrorFiles.__name__,
            PassportElementErrorTranslationFile.__name__,
            PassportElementErrorTranslationFiles.__name__,
            PassportElementErrorUnspecified.__name__
        ])
        logger.warning(
            'PassportElementError warning, expected'
            f' one of the following types: {errors}.'
        )
        self.__dict__ = kwargs


class PassportElementErrorDataField(PassportElementError):
    '''
    https://core.telegram.org/bots/api#passportelementerrordatafield
    Represents an issue in one of the data fields that was provided by the
    user. The error is considered resolved when the field's value changes.
    '''
    def __init__(
        self,
        type: Literal[
            'personal_details',
            'passport',
            'driver_license',
            'identity_card',
            'internal_passport',
            'address'
        ],
        field_name: str,
        data_hash: str,
        message: str,
        source: str = 'data'
    ):
        self.source = source
        self.type = type
        self.field_name = field_name
        self.data_hash = data_hash
        self.message = message


class PassportElementErrorFrontSide(PassportElementError):
    '''
    https://core.telegram.org/bots/api#passportelementerrorfrontside
    Represents an issue with the front side of a document. The error is
    considered resolved when the file with the front side of the document changes.
    '''
    def __init__(
        self,
        type: Literal[
            'passport',
            'driver_license',
            'identity_card',
            'internal_passport'
        ],
        file_hash: str,
        message: str,
        source: str = 'front_side'
    ):
        self.source = source
        self.type = type
        self.file_hash = file_hash
        self.message = message


class PassportElementErrorReverseSide(PassportElementError):
    '''
    https://core.telegram.org/bots/api#passportelementerrorreverseside
    Represents an issue with the reverse side of a document. The error is
    considered resolved when the file with reverse side of the document changes.
    '''
    def __init__(
        self,
        type: Literal['driver_license', 'identity_card'],
        file_hash: str,
        message: str,
        source: str = 'reverse_side'
    ):
        self.source = source
        self.type = type
        self.file_hash = file_hash
        self.message = message


class PassportElementErrorSelfie(PassportElementError):
    '''
    https://core.telegram.org/bots/api#passportelementerrorselfie
    Represents an issue with the selfie with a document. The error
    is considered resolved when the file with the selfie changes.
    '''
    def __init__(
        self,
        type: Literal[
            'passport',
            'driver_license',
            'identity_card',
            'internal_passport'
        ],
        file_hash: str,
        message: str,
        source: str = 'selfie'
    ):
        self.source = source
        self.type = type
        self.file_hash = file_hash
        self.message = message


class PassportElementErrorFile(PassportElementError):
    '''
    https://core.telegram.org/bots/api#passportelementerrorfile
    Represents an issue with a document scan. The error is
    considered resolved when the file with the document scan changes.
    '''
    def __init__(
        self,
        type: Literal[
            'utility_bill',
            'bank_statement',
            'rental_agreement',
            'passport_registration',
            'temporary_registration'
        ],
        file_hash: str,
        message: str,
        source: str = 'file'
    ):
        self.source = source
        self.type = type
        self.file_hash = file_hash
        self.message = message


class PassportElementErrorFiles(PassportElementError):
    '''
    https://core.telegram.org/bots/api#passportelementerrorfiles
    Represents an issue with a list of scans. The error is considered
    resolved when the list of files containing the scans changes.
    '''
    def __init__(
        self,
        type: Literal[
            'utility_bill',
            'bank_statement',
            'rental_agreement',
            'passport_registration',
            'temporary_registration'
        ],
        file_hashes: list[str],
        message: str,
        source: str = 'files'
    ):
        self.source = source
        self.type = type
        self.file_hashes = file_hashes
        self.message = message


class PassportElementErrorTranslationFile(PassportElementError):
    '''
    https://core.telegram.org/bots/api#passportelementerrortranslationfile
    Represents an issue with one of the files that constitute the translation
    of a document. The error is considered resolved when the file changes.
    '''
    def __init__(
        self,
        type: Literal[
            'passport',
            'driver_license',
            'identity_card',
            'internal_passport',
            'utility_bill',
            'bank_statement',
            'rental_agreement',
            'passport_registration',
            'temporary_registration'
        ],
        file_hash: str,
        message: str,
        source: str = 'translation_file'
    ):
        self.source = source
        self.type = type
        self.file_hash = file_hash
        self.message = message


class PassportElementErrorTranslationFiles(PassportElementError):
    '''
    https://core.telegram.org/bots/api#passportelementerrortranslationfiles
    Represents an issue with the translated version of a document. The error
    is considered resolved when a file with the document translation change.
    '''
    def __init__(
        self,
        type: Literal[
            'passport',
            'driver_license',
            'identity_card',
            'internal_passport',
            'utility_bill',
            'bank_statement',
            'rental_agreement',
            'passport_registration',
            'temporary_registration'
        ],
        file_hashes: list[str],
        message: str,
        source: str = 'translation_files'
    ):
        self.source = source
        self.type = type
        self.file_hashes = file_hashes
        self.message = message


class PassportElementErrorUnspecified(PassportElementError):
    '''
    https://core.telegram.org/bots/api#passportelementerrorunspecified
    Represents an issue in an unspecified place. The error is considered resolved when new data is added.
    '''
    def __init__(
        self,
        type: str,
        element_hash: str,
        message: str,
        source: str = 'unspecified'
    ):
        self.source = source
        self.type = type
        self.element_hash = element_hash
        self.message = message


class Game(TelegramType):
    '''
    https://core.telegram.org/bots/api#game
    This object represents a game. Use BotFather to create and edit games, their short names will act as unique identifiers.
    '''
    @classmethod
    def dese(cls, result):
        if result is None: return None
        obj = _check_dict(result)
        obj['title'] = obj.get('title')
        obj['description'] = obj.get('description')
        obj['photo'] = [PhotoSize.dese(kwargs) for kwargs in obj.get('photo')]
        obj['text'] = obj.get('text')
        obj['text_entities'] = [MessageEntity.dese(kwargs) for kwargs in obj.get('text_entities')] if 'text_entities' in obj else None
        obj['animation'] = Animation.dese(obj.get('animation'))
        return cls(**obj)

    def __init__(
        self,
        title: str,
        description: str,
        photo: list[PhotoSize],
        text: Optional[str] = None,
        text_entities: Optional[list[MessageEntity]] = None,
        animation: Optional[Animation] = None,
        **kwargs
    ):
        _get_kwargs(self, kwargs)
        self.title = title
        self.description = description
        self.photo = photo
        self.text = text
        self.text_entities = text_entities
        self.animation = animation


class GameHighScore(TelegramType):
    '''
    https://core.telegram.org/bots/api#gamehighscore
    This object represents one row of the high scores table for a game.
    '''
    @classmethod
    def dese(cls, result):
        if result is None: return None
        obj = _check_dict(result)
        obj['position'] = obj.get('position')
        obj['user'] = User.dese(obj.get('user'))
        obj['score'] = obj.get('score')
        return cls(**obj)

    def __init__(
        self,
        position: int,
        user: User,
        score: int,
        **kwargs
    ):
        _get_kwargs(self, kwargs)
        self.position = position
        self.user = user
        self.score = score


class GiveawayCreated(TelegramType):
    '''
    https://core.telegram.org/bots/api#giveawaycreated
    This object represents a service message about the creation of a scheduled giveaway. Currently holds no information.
    '''
    @classmethod
    def dese(cls, result):
        if result is None: return None
        obj = _check_dict(result)
        return cls(**obj)

    def __init__(
        self,
        **kwargs
    ):
        _get_kwargs(self, kwargs)
        self.__dict__ = kwargs


class GiveawayWinners(TelegramType):
    '''
    https://core.telegram.org/bots/api#giveawaywinners
    This object represents a message about the completion of a giveaway with public winners.
    '''
    @classmethod
    def dese(cls, result):
        if result is None: return None
        obj = _check_dict(result)
        obj['chat'] = Chat.dese(obj.get('chat'))
        obj['giveaway_message_id'] = obj.get('giveaway_message_id')
        obj['winners_selection_date'] = obj.get('winners_selection_date')
        obj['winner_count'] = obj.get('winner_count')
        obj['winners'] = [User.dese(kwargs) for kwargs in obj.get('winners')]
        obj['additional_chat_count'] = obj.get('additional_chat_count')
        obj['premium_subscription_month_count'] = obj.get('premium_subscription_month_count')
        obj['unclaimed_prize_count'] = obj.get('unclaimed_prize_count')
        obj['only_new_members'] = obj.get('only_new_members')
        obj['was_refunded'] = obj.get('was_refunded')
        obj['prize_description'] = obj.get('prize_description')
        return cls(**obj)

    def __init__(
        self,
        chat: Chat,
        giveaway_message_id: int,
        winners_selection_date: int,
        winner_count: int,
        winners: list[User],
        additional_chat_count: Optional[int] = None,
        premium_subscription_month_count: Optional[int] = None,
        unclaimed_prize_count: Optional[int] = None,
        only_new_members: Optional[Literal[True]] = None,
        was_refunded: Optional[Literal[True]] = None,
        prize_description: Optional[str] = None,
        **kwargs
    ):
        _get_kwargs(self, kwargs)
        self.chat = chat
        self.giveaway_message_id = giveaway_message_id
        self.winners_selection_date = winners_selection_date
        self.winner_count = winner_count
        self.winners = winners
        self.additional_chat_count = additional_chat_count
        self.premium_subscription_month_count = premium_subscription_month_count
        self.unclaimed_prize_count = unclaimed_prize_count
        self.only_new_members = only_new_members
        self.was_refunded = was_refunded
        self.prize_description = prize_description


class GiveawayCompleted(TelegramType):
    '''
    https://core.telegram.org/bots/api#giveawaycompleted
    This object represents a service message about the completion of a giveaway without public winners.
    '''
    @classmethod
    def dese(cls, result):
        if result is None: return None
        obj = _check_dict(result)
        obj['winner_count'] = obj.get('winner_count')
        obj['unclaimed_prize_count'] = obj.get('unclaimed_prize_count')
        obj['giveaway_message'] = Message.dese(obj.get('giveaway_message'))
        return cls(**obj)

    def __init__(
        self,
        winner_count: int,
        unclaimed_prize_count: Optional[int] = None,
        giveaway_message: Optional[Message] = None,
        **kwargs
    ):
        _get_kwargs(self, kwargs)
        self.winner_count = winner_count
        self.unclaimed_prize_count = unclaimed_prize_count
        self.giveaway_message = giveaway_message


class Giveaway(TelegramType):
    '''
    https://core.telegram.org/bots/api#giveaway
    This object represents a message about a scheduled giveaway.
    '''
    @classmethod
    def dese(cls, result):
        if result is None: return None
        obj = _check_dict(result)
        obj['chats'] = [Chat.dese(kwargs) for kwargs in obj.get('chats')]
        obj['winners_selection_date'] = obj.get('winners_selection_date')
        obj['winner_count'] = obj.get('winner_count')
        obj['only_new_members'] = obj.get('only_new_members')
        obj['has_public_winners'] = obj.get('has_public_winners')
        obj['prize_description'] = obj.get('prize_description')
        obj['country_codes'] = obj.get('country_codes')
        obj['premium_subscription_month_count'] = obj.get('premium_subscription_month_count')
        return cls(**obj)

    def __init__(
        self,
        chats: list[Chat],
        winners_selection_date: int,
        winner_count: int,
        only_new_members: Optional[Literal[True]] = None,
        has_public_winners: Optional[Literal[True]] = None,
        prize_description: Optional[str] = None,
        country_codes: Optional[list[str]] = None,
        premium_subscription_month_count: Optional[int] = None,
        **kwargs
    ):
        _get_kwargs(self, kwargs)
        self.chats = chats
        self.winners_selection_date = winners_selection_date
        self.winner_count = winner_count
        self.only_new_members = only_new_members
        self.has_public_winners = has_public_winners
        self.prize_description = prize_description
        self.country_codes = country_codes
        self.premium_subscription_month_count = premium_subscription_month_count


# MessageOrigin: 4 SUBCLASSES

class MessageOrigin(TelegramType):
    '''
    https://core.telegram.org/bots/api#messageorigin
    This object describes the origin of a message. It can be one of:
    - MessageOriginUser
    - MessageOriginHiddenUser
    - MessageOriginChat
    - MessageOriginChannel
    '''
    @classmethod
    def dese(cls, result):
        if result is None: return None
        obj = _check_dict(result)
        type = obj['type']

        if type == 'user':
            obj['sender_user'] = User.dese(obj.get('sender_user'))
            return MessageOriginUser(**obj)

        elif type == 'hidden_user':
            return MessageOriginHiddenUser(**obj)

        elif type == 'chat':
            obj['sender_chat'] = Chat.dese(obj.get('sender_chat'))
            return MessageOriginChat(**obj)

        elif type == 'channel':
            obj['chat'] = Chat.dese(obj.get('chat'))
            return MessageOriginChannel(**obj)
        else:
            return cls(**obj)

    def __init__(
        self,
        **kwargs
    ):
        origin_types = ', '.join([
            MessageOriginUser.__name__,
            MessageOriginHiddenUser.__name__,
            MessageOriginChat.__name__,
            MessageOriginChannel.__name__
        ])
        logger.warning(
            'MessageOrigin warning, expected one'
            f' of the following types: {origin_types}.'
        )
        self.__dict__ = kwargs


class MessageOriginUser(MessageOrigin):
    '''
    https://core.telegram.org/bots/api#messageoriginuser
    The message was originally sent by a known user.
    '''
    def __init__(
        self,
        date: int,
        sender_user: User,
        type: str = 'user',
        **kwargs
    ):
        _get_kwargs(self, kwargs)
        self.type = type
        self.date = date
        self.sender_user = sender_user


class MessageOriginHiddenUser(MessageOrigin):
    '''
    https://core.telegram.org/bots/api#messageoriginhiddenuser
    The message was originally sent by an unknown user.
    '''
    def __init__(
        self,
        date: int,
        sender_user_name: str,
        type: str = 'hidden_user',
        **kwargs
    ):
        _get_kwargs(self, kwargs)
        self.type = type
        self.date = date
        self.sender_user_name = sender_user_name


class MessageOriginChat(MessageOrigin):
    '''
    https://core.telegram.org/bots/api#messageoriginchat
    The message was originally sent on behalf of a chat to a group chat.
    '''
    def __init__(
        self,
        date: int,
        sender_chat: Chat,
        author_signature: Optional[str] = None,
        type: str = 'chat',
        **kwargs
    ):
        _get_kwargs(self, kwargs)
        self.type = type
        self.date = date
        self.sender_chat = sender_chat
        self.author_signature = author_signature


class MessageOriginChannel(MessageOrigin):
    '''
    https://core.telegram.org/bots/api#messageoriginchannel
    The message was originally sent to a channel chat.
    '''
    def __init__(
        self,
        date: int,
        chat: Chat,
        message_id: int,
        author_signature: Optional[str] = None,
        type: str = 'channel',
        **kwargs
    ):
        _get_kwargs(self, kwargs)
        self.type = type
        self.date = date
        self.chat = chat
        self.message_id = message_id
        self.author_signature = author_signature


class ExternalReplyInfo(TelegramType):
    '''
    https://core.telegram.org/bots/api#externalreplyinfo
    This object contains information about a message that is being replied to, which may come from another chat or forum topic.
    '''
    @classmethod
    def dese(cls, result):
        if result is None: return None
        obj = _check_dict(result)
        obj['origin'] = MessageOrigin.dese(obj.get('origin'))
        obj['chat'] = Chat.dese(obj.get('chat'))
        obj['message_id'] = obj.get('message_id')
        obj['link_preview_options'] = LinkPreviewOptions.dese(obj.get('link_preview_options'))
        obj['animation'] = Animation.dese(obj.get('animation'))
        obj['audio'] = Audio.dese(obj.get('audio'))
        obj['document'] = Document.dese(obj.get('document'))
        obj['photo'] = [PhotoSize.dese(kwargs) for kwargs in obj.get('photo')] if 'photo' in obj else None
        obj['sticker'] = Sticker.dese(obj.get('sticker'))
        obj['story'] = Story.dese(obj.get('story'))
        obj['video'] = Video.dese(obj.get('video'))
        obj['video_note'] = VideoNote.dese(obj.get('video_note'))
        obj['voice'] = Voice.dese(obj.get('voice'))
        obj['has_media_spoiler'] = obj.get('has_media_spoiler')
        obj['contact'] = Contact.dese(obj.get('contact'))
        obj['dice'] = Dice.dese(obj.get('dice'))
        obj['game'] = Game.dese(obj.get('game'))
        obj['giveaway'] = Giveaway.dese(obj.get('giveaway'))
        obj['giveaway_winners'] = GiveawayWinners.dese(obj.get('giveaway_winners'))
        obj['invoice'] = Invoice.dese(obj.get('invoice'))
        obj['location'] = Location.dese(obj.get('location'))
        obj['poll'] = Poll.dese(obj.get('poll'))
        obj['venue'] = Venue.dese(obj.get('venue'))
        return cls(**obj)

    def __init__(
        self,
        origin: MessageOrigin,
        chat: Optional[Chat] = None,
        message_id: Optional[int] = None,
        link_preview_options: Optional[LinkPreviewOptions] = None,
        animation: Optional[Animation] = None,
        audio: Optional[Audio] = None,
        document: Optional[Document] = None,
        photo: Optional[list[PhotoSize]] = None,
        sticker: Optional[Sticker] = None,
        story: Optional[Story] = None,
        video: Optional[Video] = None,
        video_note: Optional[VideoNote] = None,
        voice: Optional[Voice] = None,
        has_media_spoiler: Optional[Literal[True]] = None,
        contact: Optional[Contact] = None,
        dice: Optional[Dice] = None,
        game: Optional[Game] = None,
        giveaway: Optional[Giveaway] = None,
        giveaway_winners: Optional[GiveawayWinners] = None,
        invoice: Optional[Invoice] = None,
        location: Optional[Location] = None,
        poll: Optional[Poll] = None,
        venue: Optional[Venue] = None,
        **kwargs
    ):
        _get_kwargs(self, kwargs)
        self.origin = origin
        self.chat = chat
        self.message_id = message_id
        self.link_preview_options = link_preview_options
        self.animation = animation
        self.audio = audio
        self.document = document
        self.photo = photo
        self.sticker = sticker
        self.story = story
        self.video = video
        self.video_note = video_note
        self.voice = voice
        self.has_media_spoiler = has_media_spoiler
        self.contact = contact
        self.dice = dice
        self.game = game
        self.giveaway = giveaway
        self.giveaway_winners = giveaway_winners
        self.invoice = invoice
        self.location = location
        self.poll = poll
        self.venue = venue


# ChatBoostSource: 3 SUBCLASSES

class ChatBoostSource(TelegramType):
    '''
    https://core.telegram.org/bots/api#chatboostsource
    This object describes the source of a chat boost. It can be one of:
    - ChatBoostSourcePremium
    - ChatBoostSourceGiftCode
    - ChatBoostSourceGiveaway
    '''
    @classmethod
    def dese(cls, result):
        if result is None: return None
        obj = _check_dict(result)
        source = obj['source']

        obj['user'] = User.dese(obj.get('user'))

        if source == 'premium':
            return ChatBoostSourcePremium(**obj)

        elif source == 'gift_code':
            return ChatBoostSourceGiftCode(**obj)

        elif source == 'giveaway':
            return ChatBoostSourceGiveaway(**obj)
        else:
            return cls(**obj)

    def __init__(
        self,
        **kwargs
    ):
        source_types = ', '.join([
            ChatBoostSourcePremium.__name__,
            ChatBoostSourceGiftCode.__name__,
            ChatBoostSourceGiveaway.__name__
        ])
        logger.warning(
            'ChatBoostSource warning, expected one'
            f' of the following types: {source_types}.'
        )
        self.__dict__ = kwargs


class ChatBoostSourcePremium(ChatBoostSource):
    '''
    https://core.telegram.org/bots/api#chatboostsourcepremium
    The boost was obtained by subscribing to Telegram Premium or by gifting a Telegram Premium subscription to another user.
    '''
    def __init__(
        self,
        user: User,
        source: str = 'premium',
        **kwargs
    ):
        _get_kwargs(self, kwargs)
        self.source = source
        self.user = user


class ChatBoostSourceGiftCode(ChatBoostSource):
    '''
    https://core.telegram.org/bots/api#chatboostsourcegiftcode
    The boost was obtained by the creation of Telegram Premium gift codes to boost a chat. Each such
    code boosts the chat 4 times for the duration of the corresponding Telegram Premium subscription.
    '''
    def __init__(
        self,
        user: User,
        source: str = 'gift_code',
        **kwargs
    ):
        _get_kwargs(self, kwargs)
        self.source = source
        self.user = user


class ChatBoostSourceGiveaway(ChatBoostSource):
    '''
    The boost was obtained by the creation of a Telegram Premium giveaway. This boosts
    the chat 4 times for the duration of the corresponding Telegram Premium subscription.
    '''
    def __init__(
        self,
        giveaway_message_id: int,
        user: Optional[User] = None,
        is_unclaimed: Optional[Literal[True]] = None,
        source: str = 'giveaway',
        **kwargs
    ):
        _get_kwargs(self, kwargs)
        self.source = source
        self.giveaway_message_id = giveaway_message_id
        self.user = user
        self.is_unclaimed = is_unclaimed


class ChatBoost(TelegramType):
    '''
    https://core.telegram.org/bots/api#chatboost
    This object contains information about a chat boost.
    '''
    @classmethod
    def dese(cls, result):
        if result is None: return None
        obj = _check_dict(result)
        obj['boost_id'] = obj.get('boost_id')
        obj['add_date'] = obj.get('add_date')
        obj['expiration_date'] = obj.get('expiration_date')
        obj['source'] = ChatBoostSource.dese(obj.get('source'))
        return cls(**obj)

    def __init__(
        self,
        boost_id: str,
        add_date: int,
        expiration_date: int,
        source: ChatBoostSource,
        **kwargs
    ):
        _get_kwargs(self, kwargs)
        self.boost_id = boost_id
        self.add_date = add_date
        self.expiration_date = expiration_date
        self.source = source


class UserChatBoosts(TelegramType):
    '''
    https://core.telegram.org/bots/api#userchatboosts
    This object represents a list of boosts added to a chat by a user.
    '''
    @classmethod
    def dese(cls, result):
        if result is None: return None
        obj = _check_dict(result)
        obj['boosts'] = [ChatBoost.dese(kwargs) for kwargs in obj.get('boosts')]
        return cls(**obj)

    def __init__(
        self,
        boosts: list[ChatBoost],
        **kwargs
    ):
        _get_kwargs(self, kwargs)
        self.boosts = boosts


class ChatBoostUpdated(TelegramType):
    '''
    https://core.telegram.org/bots/api#chatboostupdated
    This object represents a boost added to a chat or changed.
    '''
    @classmethod
    def dese(cls, result):
        if result is None: return None
        obj = _check_dict(result)
        obj['chat'] = Chat.dese(obj.get('chat'))
        obj['boost'] = ChatBoost.dese(obj.get('boost'))
        return cls(**obj)

    def __init__(
        self,
        chat: Chat,
        boost: ChatBoost,
        **kwargs
    ):
        _get_kwargs(self, kwargs)
        self.chat = chat
        self.boost = boost


class ChatBoostRemoved(TelegramType):
    '''
    https://core.telegram.org/bots/api#chatboostremoved
    This object represents a boost removed from a chat.
    '''
    @classmethod
    def dese(cls, result):
        if result is None: return None
        obj = _check_dict(result)
        obj['chat'] = Chat.dese(obj.get('chat'))
        obj['boost_id'] = obj.get('boost_id')
        obj['remove_date'] = obj.get('remove_date')
        obj['source'] = ChatBoostSource.dese(obj.get('source'))
        return cls(**obj)

    def __init__(
        self,
        chat: Chat,
        boost_id: str,
        remove_date: int,
        source: ChatBoostSource,
        **kwargs
    ):
        _get_kwargs(self, kwargs)
        self.chat = chat
        self.boost_id = boost_id
        self.remove_date = remove_date
        self.source = source


class Update(TelegramType):
    '''
    https://core.telegram.org/bots/api#update
    This object represents an incoming update. At most one of
    the optional parameters can be present in any given update.
    '''
    @classmethod
    def dese(cls, result):
        if result is None: return None
        obj = _check_dict(result)
        obj['update_id'] = obj.get('update_id')
        obj['message'] = Message.dese(obj.get('message'))
        obj['edited_message'] = Message.dese(obj.get('edited_message'))
        obj['channel_post'] = Message.dese(obj.get('channel_post'))
        obj['edited_channel_post'] = Message.dese(obj.get('edited_channel_post'))
        obj['message_reaction'] = MessageReactionUpdated.dese(obj.get('message_reaction'))
        obj['message_reaction_count'] = MessageReactionCountUpdated.dese(obj.get('message_reaction_count'))
        obj['inline_query'] = InlineQuery.dese(obj.get('inline_query'))
        obj['chosen_inline_result'] = ChosenInlineResult.dese(obj.get('chosen_inline_result'))
        obj['callback_query'] = CallbackQuery.dese(obj.get('callback_query'))
        obj['shipping_query'] = ShippingQuery.dese(obj.get('shipping_query'))
        obj['pre_checkout_query'] = PreCheckoutQuery.dese(obj.get('pre_checkout_query'))
        obj['poll'] = Poll.dese(obj.get('poll'))
        obj['poll_answer'] = PollAnswer.dese(obj.get('poll_answer'))
        obj['my_chat_member'] = ChatMemberUpdated.dese(obj.get('my_chat_member'))
        obj['chat_member'] = ChatMemberUpdated.dese(obj.get('chat_member'))
        obj['chat_join_request'] = ChatJoinRequest.dese(obj.get('chat_join_request'))
        obj['chat_boost'] = ChatBoostUpdated.dese(obj.get('chat_boost'))
        obj['removed_chat_boost'] = ChatBoostRemoved.dese(obj.get('removed_chat_boost'))
        return cls(**obj)

    def __init__(
        self,
        update_id: int,
        message: Optional[Message] = None,
        edited_message: Optional[Message] = None,
        channel_post: Optional[Message] = None,
        edited_channel_post: Optional[Message] = None,
        message_reaction: Optional[MessageReactionUpdated] = None,
        message_reaction_count: Optional[MessageReactionCountUpdated] = None,
        inline_query: Optional[InlineQuery] = None,
        chosen_inline_result: Optional[ChosenInlineResult] = None,
        callback_query: Optional[CallbackQuery] = None,
        shipping_query: Optional[ShippingQuery] = None,
        pre_checkout_query: Optional[PreCheckoutQuery] = None,
        poll: Optional[Poll] = None,
        poll_answer: Optional[PollAnswer] = None,
        my_chat_member: Optional[ChatMemberUpdated] = None,
        chat_member: Optional[ChatMemberUpdated] = None,
        chat_join_request: Optional[ChatJoinRequest] = None,
        chat_boost: Optional[ChatBoostUpdated] = None,
        removed_chat_boost: Optional[ChatBoostRemoved] = None,
        **kwargs
    ):
        _get_kwargs(self, kwargs)
        self.update_id = update_id
        self.message = message
        self.edited_message = edited_message
        self.channel_post = channel_post
        self.edited_channel_post = edited_channel_post
        self.message_reaction = message_reaction
        self.message_reaction_count = message_reaction_count
        self.inline_query = inline_query
        self.chosen_inline_result = chosen_inline_result
        self.callback_query = callback_query
        self.shipping_query = shipping_query
        self.pre_checkout_query = pre_checkout_query
        self.poll = poll
        self.poll_answer = poll_answer
        self.my_chat_member = my_chat_member
        self.chat_member = chat_member
        self.chat_join_request = chat_join_request
        self.chat_boost = chat_boost
        self.removed_chat_boost = removed_chat_boost
