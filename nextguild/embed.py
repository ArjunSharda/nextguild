# -*- coding: utf-8 -*-
class EmbedField:
    def __init__(self, name: str, value: str, inline: bool = False):
        super().__init__()
        self.name = name
        self.value = value
        self.inline = inline


class Embed:
    def __init__(
            self,
            title: str = None,
            description: str = None,
            color: int or str = None,
            author: str = None,
            author_url: str = None,
            author_icon: str = None,
            footer: str = None,
            footer_icon: str = None,
            thumbnail_url: str = None,
            image_url: str = None,
            fields: list[EmbedField] | dict = None
    ):
        self.title = title
        self.description = description
        self.color = color
        if isinstance(color, str):
            if color.startswith('#'):
                self.color = int(color[1:], 16)
            elif color.startswith('0x'):
                self.color = int(color[2:], 16)
        self.color = color
        self.author = author
        self.author_url = author_url
        self.author_icon = author_icon
        self.footer = footer
        self.footer_icon = footer_icon
        self.thumbnail_url = thumbnail_url
        self.image_url = image_url
        self.__fields = []
        if fields:
            for field in fields:
                if isinstance(field, EmbedField):
                    self.add_field(field.name, field.value, field.inline)
                elif isinstance(field, dict):
                    self.add_field(field.get('name'), field.get('value'), field.get('inline'))

    @property
    def to_dict(self) -> dict:
        embed = {}

        if self.title:
            embed.update({'title': self.title})

        if self.description:
            embed.update({'description': self.description})

        if self.color:
            embed.update({'color': self.color})

        if self.author or self.author_url or self.author_icon:
            author_dict = {}
            if self.author:
                author_dict.update({'name': self.author})
            if self.author_url:
                author_dict.update({'url': self.author_url})
            if self.author_icon:
                author_dict.update({'iconUrl': self.author_icon})
            embed.update({'author': author_dict})

        if self.footer or self.footer_icon:
            footer_dict = {}
            if self.footer:
                footer_dict.update({'text': self.footer})
            if self.footer_icon:
                footer_dict.update({'iconUrl': self.footer_icon})
            embed.update({'footer': footer_dict})

        if self.thumbnail_url:
            embed.update({'thumbnail': {'url': self.thumbnail_url}})

        if self.image_url:
            embed.update({'image': {'url': self.image_url}})

        fields_list = []
        for field in self.__fields:
            fields_list.append({'name': field.name, 'value': field.value, 'inline': field.inline})
        embed.update({'fields': fields_list})

        return embed

    @property
    def fields(self) -> list:
        return self.__fields

    def add_field(self, name: str, value: str, inline: bool = False) -> None:
        inline = str(inline).lower()
        self.__fields.append(EmbedField(name, value, inline))

    def remove_field(self, index: int) -> None:
        self.__fields.pop(index)

    def insert_field(self, index: int, name: str, value: str) -> None:
        self.__fields.insert(index, EmbedField(name, value))
