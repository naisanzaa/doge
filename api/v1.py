from automon.helpers.dictWrapper import DictUpdate


class ApiBase(object):
    """The base URL for all API endpoints is https://www.ecfr.gov.
    """
    url: str = 'https://www.ecfr.gov'


class ApiAdmin(object):

    def __init__(self):
        pass

    def agencies(self):
        """All top-level agencies in name order with children also in name order

        No parameters
        """
        return f'{ApiBase.url}/api/admin/v1/agencies.json'

    def corrections(self):
        """The Corrections service can be used to determine all corrections or can be filtered by title, effective date,
        or correction date.

        Parameters
        Name	Description
        date
        string
        (query)
        Restricts results to eCFR corrections that occurred on or before the specified date and that were corrected on or after the specified date. Format: YYYY-MM-DD

        title
        string
        (query)
        Restricts results to the given title number: Format: '1’, '2’, '50’, etc

        error_corrected_date
        string
        (query)
        Returns only corrections that were corrected on the given date. Format: YYYY-MM-DD
        """
        return f'{ApiBase.url}/api/admin/v1/corrections.json'

    def corrections_title(self, title: str):
        """The Corrections service can be used to determine all corrections for the given title.

        Parameters
        Name	Description
        title *
        string
        (path)
        Restricts results to the given title number: Format: '1’, '2’, '50’, etc
        """

        return f'{ApiBase.url}/api/admin/v1/corrections/title/{title}.json'


class ApiVersioner(object):

    def __init__(self):
        pass

    def full(
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
    ):
        """The title source route can be used to retrieve the source xml for a complete title or subset. The subset of xml is determined by the lowest leaf node given. For example, if you request Title 1, Chapter I, Part 1, you’ll receive the XML only for Part 1 and its children.
        If you request a section you’ll receive the section XML inside its parent Part as well as relevant non-section sibling nodes (Auth, Source, etc).
        The largest title source xml files can be dozens of megabytes.

        GPO eCFR XML User guide

        Parameters
        Name	Description
        date *
        string
        (path)
        YYYY-MM-DD

        title *
        string
        (path)
        Title Number: '1’, '2’, '50’, etc

        subtitle
        string
        (query)
        Uppercase letter. 'A’, 'B’, ‘C’

        chapter
        string
        (query)
        Roman Numerals and digits 0-9. 'I’, 'X’, ‘1’

        subchapter
        string
        (query)
        A SUBCHAPTER REQUIRES A CHAPTER. Uppercase letters with optional underscore or dash. 'A’, 'B’, ‘I’

        part
        string
        (query)
        Uppercase letters with optional underscore or dash. 'A’, 'B’, ‘I’

        subpart
        string
        (query)
        A SUBPART REQUIRES A PART. Generally an uppercase letter. 'A’, 'B’, ‘C’

        section
        string
        (query)
        A SECTION REQUIRES A PART. Generally a number followed by a dot and another number. '121.1’, '13.4’, ‘1.9’

        appendix
        string
        (query)
        AN APPENDIX REQUIRES A SUBTITLE, CHAPTER or PART. Multiple formats. 'A’, 'III’, ‘App. A’
        """
        return f'{ApiBase.url}/api/versioner/v1/full/{date}/title-{title}.xml'


class AgenciesClass(DictUpdate):

    def __init__(self):
        super().__init__()


class VersionerFullClass(DictUpdate):
    pass
