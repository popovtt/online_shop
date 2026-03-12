class EnumFilter:
    title = "Category"
    parameter_name = "category"

    def __init__(self, column, enum_cls):
        self.column = column
        self.enum_cls = enum_cls

    def lookups(self, request, model, run_query):
        return [(e.value, e.value) for e in self.enum_cls]

    async def get_filtered_query(self, query, value, model):
        if not value:
            return query
        # value is a string from query params, match your enum accordingly
        return query.filter(self.column == self.enum_cls(value))
