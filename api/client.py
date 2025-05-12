import json
import xml
import xml.dom.minidom

from automon.integrations.requestsWrapper import RequestsClient

from .v1 import *

DEBUG = 2


def debug(log: str, level: int = 1):
    if DEBUG == level:
        print(log)


class EcfrClient(object):

    def __init__(self):
        self._requests = RequestsClient()

        self.agencies: list = None
        self.versioner_full: dict = {}

    @property
    def _response(self):
        return self._requests.response

    @property
    def _errors(self):
        return self._requests.errors

    @property
    def _content(self):
        return self._requests.content

    @property
    def _text(self):
        return self._requests.text

    def to_json(self):
        return json.loads(self._text)

    def to_xml(self):
        return xml.dom.minidom.parseString(self._text)

    def get_agencies(self):
        url = ApiAdmin().agencies()

        self._requests.get(url=url)
        self.agencies = [AgenciesClass().update_dict(x) for x in self.to_json().get('agencies')]

        debug(f'EcfrClient :: get_agencies :: {len(self.agencies)} agencies', level=2)
        debug(f'EcfrClient :: get_agencies :: done', level=1)
        return self

    def get_versioner_full(
            self,
            date: str,
            title: str,
            subtitle: str = None,
            chapter: str = None,
            subchapter: str = None,
            part: str = None,
            subpart: str = None,
            section: str = None,
            appendix: str = None,
            **kwargs
    ):
        url = ApiVersioner().full(date=date, title=title)

        params = dict(
            subtitle=subtitle,
            chapter=chapter,
            subchapter=subchapter,
            part=part,
            subpart=subpart,
            section=section,
            appendix=appendix
        )

        self._requests.get(url=url, params=params, **kwargs)

        versioner_full = dict(
            date=date,
            title=title,
            subtitle=subtitle,
            chapter=chapter,
            subchapter=subchapter,
            part=part,
            subpart=subpart,
            section=section,
            appendix=appendix,
            xml=self._text,
            size_bytes=len(self._text),
            size_kilobytes=round(len(self._text) / 1024),
            size_megabytes=round(len(self._text) / 1024 / 1024, 2),
        )
        self.versioner_full[title] = versioner_full

        debug(f'EcfrClient :: get_versioner_full :: {title=} :: {versioner_full["size_megabytes"]=} MB', level=2)
        debug(f'EcfrClient :: get_versioner_full :: done', level=1)
        return self
