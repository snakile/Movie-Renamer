class ImdbQuery(str):
    def exclude_terms(self, tems_to_exclude):
        r = self
        for term in tems_to_exclude: r = r.replace(term, ' ')
        return ImdbQuery(r.lstrip().rstrip())
    
    def lower(self):
        return ImdbQuery(super(ImdbQuery, self).lower())