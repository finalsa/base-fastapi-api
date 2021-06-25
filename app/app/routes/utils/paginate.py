import ormar as orm
import math
from typing import List, Optional, Union


async def load_data_callback(result=[]):
    for r in result:
        await r.load_data()
    return result


class Pagination():

    def __init__(
        self,
        pagination: Optional[bool] = False,
        search: Optional[str] = None,
        objects_per_page: Optional[int] = 10,
        page: Optional[int] = 0,
        limit: Optional[int] = 10,
        order_by: Optional[str] = '-id',
    ):
        self.pagination = pagination
        self.objects_per_page = objects_per_page
        self.page = page
        self.limit = limit
        self.order_by = order_by.split(",")
        self.search = search
        self.filters = {}

    def set_filters(self, **filters):
        if("pagination" in filters):
            filters.pop("pagination")
        if("objects_per_page" in filters):
            filters.pop("pagination")
        if("page" in filters):
            filters.pop("page")
        if("limit" in filters):
            filters.pop("limit")
        if("order_by" in filters):
            filters.pop("order_by")
        self.filters = filters

    def __str__(self) -> str:
        return "pagination:{}, objects_per_page:{}, page:{}, limit:{}, order_by:{}, filters:{}".format(
            self.pagination,
            self.objects_per_page,
            self.page,
            self.limit,
            self.order_by,
            self.filters
        )


async def paginate_without_object(
    model: orm.Model,
    options: Pagination = Pagination(),
    callback=None,
    search_attributes=[]
):
    result = []
    if(options.limit == 0):
        offset = options.objects_per_page * options.page
        result = await model.offset(
            offset
        ).limit(
            options.objects_per_page
        ).order_by(
            options.order_by
        ).all(**options.filters)
    else:
        offset = options.objects_per_page * options.page
        result = await model.offset(
            offset
        ).limit(
            options.limit
        ).order_by(
            options.order_by
        ).all(**options.filters)
    if(callback is not None and len(callback) > 1):
        callback[1]['result'] = result
        result = await callback[0](** callback[1])
    if(options.pagination):
        total_objects = await model.filter(
            **options.filters
        ).count()
        total_pages = math.floor(total_objects / options.objects_per_page)
        if(total_objects % options.objects_per_page) > 0:
            total_pages += 1
        r = {
            'items_per_page':  options.objects_per_page,
            'total_objects': total_objects,
            'total_pages': total_pages,
            'actual_page': options.page,
            'data': result
        }
        return r
    else:
        return result


async def paginate_object(
    model: orm.Model,
    options: Pagination = Pagination(),
    callback=None,
    search_attributes=[]
):
    result = []
    if(options.limit == 0):
        offset = options.objects_per_page * options.page
        result = await model.objects.offset(
            offset
        ).limit(
            options.objects_per_page
        ).order_by(
            options.order_by
        ).all(**options.filters)
    else:
        offset = options.objects_per_page * options.page
        result = await model.objects.offset(
            offset
        ).limit(
            options.limit
        ).order_by(
            options.order_by
        ).all(**options.filters)
    if(callback is not None and len(callback) > 1):
        callback[1]['result'] = result
        result = await callback[0](** callback[1])
    if(options.pagination):
        total_objects = await model.objects.filter(
            **options.filters
        ).count()
        total_pages = math.floor(total_objects / options.objects_per_page)
        if(total_objects % options.objects_per_page) > 0:
            total_pages += 1
        r = {
            'items_per_page':  options.objects_per_page,
            'total_objects': total_objects,
            'total_pages': total_pages,
            'actual_page': options.page,
            'data': result
        }
        return r
    else:
        return result
