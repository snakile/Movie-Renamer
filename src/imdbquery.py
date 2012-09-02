import re
import terms_to_exclude_before_splitting
import terms_to_exclude_after_splitting

class ImdbQuery(str):
    @staticmethod
    def create_query_from_filename(filename):
        terms_before = terms_to_exclude_before_splitting.terms
        terms_after = terms_to_exclude_after_splitting.terms
        query = ImdbQuery(filename). \
                exclude_terms(terms_before).lower(). \
                remove_non_alaphnumeric_chars(). \
                exclude_terms(terms_after). \
                add_parentheses_around_years()
        return query
    
    def exclude_terms(self, terms_to_exclude):
        r = self
        for term in terms_to_exclude: r = r.replace(term, ' ')
        return ImdbQuery(r.lstrip().rstrip())
    
    def remove_non_alaphnumeric_chars(self):
        terms = re.compile(r'[^a-zA-Z0-9]+').split(self)
        return ImdbQuery(' '.join(terms)).lstrip().rstrip()
    
    def add_parentheses_around_years(self):
        regex = re.compile(r'(19|20)\d{2}')
        return ImdbQuery(regex.sub(lambda m: '({0})'.format(m.group(0)), self))
    
    def lower(self):
        return ImdbQuery(super(ImdbQuery, self).lower())
    
    def lstrip(self):
        return ImdbQuery(super(ImdbQuery, self).lstrip())
    
    def rstrip(self):
        return ImdbQuery(super(ImdbQuery, self).rstrip())
