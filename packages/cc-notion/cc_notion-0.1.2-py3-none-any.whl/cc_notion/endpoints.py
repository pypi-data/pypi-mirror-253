#!/usr/bin/env python3

from typing import Any, TYPE_CHECKING
if TYPE_CHECKING:
    from .client import BaseClient
from .typing import SyncAsync
from .helpers import pick
import pandas
from collections import OrderedDict


class Endpoint:

    def __init__(self, parent: "BaseClient") -> None:
        self.parent = parent


class BlocksChildrenEndpoint(Endpoint):

    def append(self, block_id: str, **kwargs: Any) -> SyncAsync[Any]:
        return self.parent.request(
            path=f'blocks/{block_id}/children',
            method='PATCH',
            body=pick(kwargs, 'children', 'after'),
            auth=kwargs.get('auth')
        )
    
    def list(self, block_id: str, **kwargs: Any) -> SyncAsync[Any]:
        return self.parent.request(
            path=f'blocks/{block_id}/children',
            method='GET',
            query=pick(kwargs, 'start_cursor', 'page_size'),
            auth=kwargs.get('auth')
        )

class BlocksEndpoint(Endpoint):

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.children = BlocksChildrenEndpoint(*args, **kwargs)
    
    def retrieve(self, block_id: str, **kwargs: Any) -> SyncAsync[Any]:
        return self.parent.request(
            path=f'blocks/{block_id}', method='GET', auth=kwargs.get('auth')
        )
    
    def update(self, block_id: str, **kwargs: Any) -> SyncAsync[Any]:
        return self.parent.request(
            path=f'blocks/{block_id}',
            method='PATCH',
            body=pick(
                kwargs,
                'emend',
                'type',
                'archived',
                "bookmark",
                "image",
                "video",
                "pdf",
                "file",
                "audio",
                "code",
                "equation",
                "divider",
                "breadcrumb",
                "table_of_contents",
                "link_to_page",
                "table_row",
                "heading_1",
                "heading_2",
                "heading_3",
                "paragraph",
                "bulleted_list_item",
                "numbered_list_item",
                "quote",
                "to_do",
                "toggle",
                "template",
                "callout",
                "synced_block",
                "table",
            ),
            auth=kwargs.get('auth')
        )
    
    def delete(self, block_id: str, **kwargs: Any) -> SyncAsync[Any]:
        return self.parent.request(
            path=f'blocks/{block_id}',
            method='DELETE',
            auth=kwargs.geT('auth')
        )


class DatabasesEndpoint(Endpoint):

    def list(self, **kwargs: Any) -> SyncAsync[Any]:
        return self.parent.request(
            path="databases",
            method="GET",
            query=pick(kwargs, "start_cursor", "page_size"),
            auth=kwargs.get("auth")
        )
    
    def query(self, database_id: str, **kwargs: Any) -> SyncAsync[Any]:
        '''
        查询 database 的所有内容, 需要传入 filter_dict

        Args:
            database_id (str): _description_

        Returns:
            SyncAsync[Any]: _description_
        '''
        return self.parent.request(
            path=f'databases/{database_id}/query',
            method="POST",
            query=pick(kwargs, "filter_properties"),
            body=pick(kwargs, "filter", "sorts", "start_cursor", "page_size"),
            auth=kwargs.get("auth")
        )
    



class PagesPropertiesEndpoint(Endpoint):

    def retrieve(self, page_id: str, property_id: str, **kwargs: Any) -> SyncAsync[Any]:
        return self.parent.request(
            path=f'pages/{page_id}/properties/{property_id}',
            method='GET',
            auth=kwargs.get('auth'),
            query=pick(kwargs, "start_cursor", "page_size")
        )


class PagesEndpoint(Endpoint):

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.properties = PagesPropertiesEndpoint(*args, **kwargs)

    def create(self, **kwargs: Any) -> SyncAsync[Any]:
        return self.parent.request(
            path='pages',
            method='POST',
            body=pick(kwargs, 'parent', 'properties', 'children', 'icon', 'cover'),
            auth=kwargs.get('auth')
        )
    
    def retrieve(self, page_id: str, **kwargs: Any) -> SyncAsync[Any]:
        return self.parent.request(
            path=f'pages/{page_id}', method='GET', auth=kwargs.get('auth')
        )

    def update(self, page_id: str, **kwargs: Any) -> SyncAsync[Any]:
        '''
        https://developers.notion.com/reference/patch-page

        Args:
            page_id (str): _description_

        Returns:
            SyncAsync[Any]: _description_
        '''
        return self.parent.request(
            path=f'pages/{page_id}',
            method='PATCH',
            body=pick(kwargs, 'archived', 'properties', 'icon', 'cover'),
            auth=kwargs.get('auth')
        )

    def create_and_check_field(self, check_database_id, check_property, check_value, **kwargs) -> SyncAsync[Any]:
        resp = self.parent.extensions.check_insertd(database_id=check_database_id, check_property=check_property, check_value=check_value)
        if resp == '未插入':
            return self.parent.request(
                path='pages',
                method='POST',
                body=pick(kwargs, 'parent', 'properties', 'children', 'icon', 'cover'),
                auth=kwargs.get('auth')
            )
        else:
            return resp

    def create_check_field_update(self, check_database_id, check_property, check_value, propertys, **kwargs) -> SyncAsync[Any]:
        resp = self.parent.extensions.check_insertd(database_id=check_database_id, 
                                                    check_property=check_property, 
                                                    check_value=check_value)
        if resp == '未插入':
            page = self.parent.build.page(database_id=check_database_id, propertys=propertys)
            return self.create(**page)
        else:
            page = self.parent.build.page(database_id=check_database_id, propertys=propertys)
            return self.update(page_id=resp, **page)

    def create_update_delete(self, 
                             database_id, 
                             check_property, 
                             check_value, 
                             propertys,
                             source_list,
                             filter_property,
                             filter_value,
                             **kwargs) -> SyncAsync[Any]:
        '''
        创建页面, 创建时会检查是否存在, 并删除源列表中不存在的页面

        Args:
            database_id (_type_): 待操作的 database_id
            check_property (_type_): 需要检查的列的名称
            check_value (_type_): 需要检查的列的值
            propertys (_type_): 待创建的页面, 需要借助 self.parent.build.page 函数, 示例格式如下
                propertys = [
                    ('title', 'Name', i.name),
                    ('rich_text', 'instance_id', i.instance_id),
                    ('status', 'instance_state', i.instance_state),
                    ('select', 'instance_type', i.instance_type),
                    ('rich_text', 'private_ip_address', i.private_ip_address),
                    ('date', 'launch_time', i.launch_time.strftime('%Y-%m-%dT%H:%M:%SZ')),
                    ('relation', '平台列表', self.paltform_relation),
                    ('rich_text', 'tags', i.tags),
                    ('select', 'availability_zone', i.availability_zone)
                ]

        Returns:
            SyncAsync[Any]: _description_
        '''
        resp = self.parent.extensions.check_insertd(database_id=database_id, check_property=check_property, check_value=check_value)
        if resp == '未插入':
            page = self.parent.build.page(database_id=database_id, propertys=propertys)
            self.create(**page)
        else:
            page = self.parent.build.page(database_id=database_id, propertys=propertys)
            return self.update(page_id=resp, **page)

        try:
            resp2 = self.parent.extensions.delete_notion(database_id=self.database_id_vm,
                                                    source_list=source_list,
                                                    property_name=check_property,
                                                    filter_property=filter_property,
                                                    filter_value=filter_value)
            return resp2
        except IndexError as e:
            raise IndexError
            log.warning(msg=e)

    

class UsersEndpoint(Endpoint):

    def list(self, **kwargs: Any):
        return self.parent.request(
            path="users",
            method="GET",
            query=pick(kwargs, "start_cursor", "page_size"),
            auth=kwargs.get('auth')
        )


class BuildEndpoint(Endpoint):

    def title(self, content):
        title = { 'title': [{ "text": { "content": content }}]}
        return title

    def rich_text(self, content):
        rich_text = { "rich_text": [{"text": {"content": content}}]}
        return rich_text
    
    def select(self, content):
        select = {"select": {"name": content}}
        return select
    
    def people(self, content):
        people = {
            "people": [{
            "object": "user",
            "id": content
            }]
        }
        return people

    def status(self, content):
        status = {"status": {"name": content}}
        return status

    def date(self, content: str, time_zone: str='Asia/Shanghai'):
        if ',' in content:
            start, end = content.split(',')[0], content.split(',')[1]
            if start == 'end':
               date = {
                    "date": {"end": end}}
            else:
                date = {
                    "date": {"start": start, "end": end, "time_zone": 'Asia/Shanghai'}}
        else:
            date = {"date": {"start": content}}
        return date

    def number(self, content: str):
        number = {'number': content}
        return number

    def relation(self, content):
        relation = {
            "relation": [
                { "id": content }
            ]
        }
        return relation

    def page(self, database_id, propertys: list) -> dict:
        '''
        _summary_

        Args:
            database_id (_type_): _description_
            propertys (list): example [(status, 'Status', '运行中'), (select, '类型', '日常工作')]

        Raises:
            ValueError: _description_

        Returns:
            dict: _description_
        '''
        properties = {}
        for property in propertys:
            if property[0] == 'status':
                properties[property[1]] = self.status(content=property[2])
            elif property[0] == 'select':
                properties[property[1]] = self.select(content=property[2])
            elif property[0] == 'date':
                properties[property[1]] = self.date(content=property[2])
            elif property[0] == 'rich_text':
                properties[property[1]] = self.rich_text(content=property[2])
            elif property[0] == 'people':
                properties[property[1]] = self.people(content=property[2])
            elif property[0] == 'relation':
                properties[property[1]] = self.relation(content=property[2])
            elif property[0] == 'title':
                properties[property[1]] = self.title(content=property[2])
            elif property[0] == 'number':
                properties[property[1]] = self.number(content=property[2])
            elif property[0] == 'multi_select':
                properties[property[1]] = self.multi_select(content=property[2])
            else:
                raise ValueError('未识别的 property')
            
        page = {
            "parent": { "database_id": database_id},
            "properties": properties
        }

        return page
    
    def filter3(self, 
               filter_property: str='name2', 
               filter_type: str='rich_text', 
               filter_value: str=''):
        
        filter = {
            "filter": {
                "property": filter_property,
                filter_type: {
                    "equals": filter_value
                }
            }
        }
        return filter

    def filter(self, filter_type: str='and', filter_syntax: list=''):
        '''
        _summary_

        Args:
            filter_type (str, optional): and 或 or, 默认是 'and'.
            filter_syntax (list, optional): 示例如下
                filter_syntax = [
                    ('status', 'Tags', 'equals', 'available'),
                    ('select', 'Type', 'equals', 'Prod')
                ]

        Returns:
            _type_: filter_dict
        '''
        filter_list = []
        for i in filter_syntax:
            test = { "property": i[1], i[0]: { i[2]: i[3]}}
            filter_list.append(test)

        return { "filter": { filter_type: filter_list } }

    def block_code(self, content, language: str='plain text'):
        return {
            "type": "code",
            "code": {
                "caption": [],
                    "rich_text": [{
                "type": "text",
                "text": {
                    "content": content
                }
                }],
                "language": "javascript"
            }
            }

    def block_toggle(self, content, children):
        return {
            "type": "toggle",
            "toggle": {
                "rich_text": [{
                "type": "text",
                "text": {
                    "content": content,
                }
                }],
                "color": "default",
                "children":[children]
            }
            }

    def block_rich_text(self, content):
        return {
            "type": "text",
            "text": {
                "content": "Some words ",
                "link": null
            },
            "annotations": {
                "bold": false,
                "italic": false,
                "strikethrough": false,
                "underline": false,
                "code": false,
                "color": "default"
            },
            "plain_text": "Some words ",
            "href": null
            }


class ExtensionsEndpoint(Endpoint):

    def check_insertd(self, database_id, check_property, check_value):
        resp = self.parent.databases.query(
            **{
                "database_id": database_id,
                "filter": {
                    "property": check_property,
                    "rich_text": {
                        "contains": check_value,
                    },
                },
            }
        )
        if resp.results:
            return self.parse_page(page=resp.results, get='page_id')
        else:
            return '未插入'
    
    def parse_page(self, page: str='', get: str='properties', name: str='none', relation_db_id: str='none'):
        '''
        _summary_

        Args:
            page (str, optional): _description_. Defaults to ''.
            get (str, optional): _description_. Defaults to 'properties'.
            name (str, optional): _description_. Defaults to 'none'.
            relation_db_id (str, optional): _description_. Defaults to 'none'.

        Returns:
            _type_: _description_
        '''
        if get == 'properties':
            column_type = page['properties'][name]['type']
            if column_type == 'select':
                result = page['properties'][name]['select']['name']
            if column_type == 'multi_select':
                result = []
                multi_selects = page['properties'][name]['multi_select']
                for multi_select in multi_selects:
                    result.append(multi_select['name'])
                return result
            elif column_type == 'status':
                result = page['properties'][name]['status']['name']
            elif column_type == 'rich_text':
                try:
                    result = page['properties'][name]['rich_text'][0]['plain_text']
                except IndexError:
                    result = 'index_error'
                except Exception as e:
                    result = e
            elif column_type == 'title':
                result = page['properties'][name]['title'][0]['plain_text']
            elif column_type == 'formula':
                result = page['properties'][name]['formula']['string']
            elif column_type == 'number':
                result = page['properties'][name]['number']
            elif column_type == 'people':
                result = page['properties'][name]['people'][0]['name']
            elif column_type == 'date':
                if page['properties'][name]['date']:
                    result = page['properties'][name]['date']['start']
                else:
                    result = '未解析到日期'
            elif column_type == 'relation':
                try:
                    relation_id = page['properties'][name]['relation'][0]['id']

                    filter_syntax = [
                            ('rich_text', 'name2', 'equals', 'name')
                        ]
                    
                    filter_dict = self.parent.build.filter(filter_syntax=filter_syntax)
                    page = self.parent.databases.query(
                        database_id=relation_id,
                        **filter_dict
                    ).results
                    result = self.parse_page(page=page, name=name)
                    # result = self.query_database_row_name(database_id=relation_db_id, page_id=relation_id, query_property='name2')
                except Exception as e:
                    result = 'error', page['properties']
            elif column_type == 'phone_number':
                result = page['properties'][name]['phone_number']
            else:
                pass
        elif get == 'page_id':
            if isinstance(page, list):
                result = page[0]['id']
            else:
                result = page['id']
        elif get == 'url':
            result = page['url']
        return result

    def parse_value(self, value):
        if value['type'] == 'select':
            result = value['select']['name']
        elif value['type'] == 'rich_text':
            result = value['rich_text'][0]['plain_text']
        elif value['type'] == 'status':
            result = value['status']['name']
        elif value['type'] == 'title':
            result = value['title'][0]['plain_text']
        else:
            result = '无法解析'

        return result

    def delete_notion(self, 
                      database_id: str='', 
                      source_list: list='',
                      property_name: str='', 
                      filter_property: str='', 
                      filter_value: str=''):
        '''
        根据提供的列表与 notion 中的做对比, 如果源列表比 notion 少, 那么会删除 notion 的页面

        Args:
            database_id (_type_): _description_
            source_list (list): _description_
            property_name (str): _description_

        Returns:
            _type_: _description_
        '''
        notion_list = []
        if filter_property:
            resp = self.parent.databases.query(database_id=database_id,
                        **{
                            "filter": {
                                "property": filter_property,
                                "rich_text": {
                                    "equals": filter_value
                                }
                            }
                        })
        else:
            resp = self.parent.databases.query(database_id=database_id)
        for result in resp.results:
            notion_list.append(self.parent.extensions.parse_page(page=result, name=property_name))
        
        to_be_delete = list(set(notion_list) - set(source_list))

        if to_be_delete:
            for i in to_be_delete:
                resp = self.parent.databases.query(database_id=database_id, 
                    **{
                        "filter": {
                            "property": property_name,
                            "rich_text": {
                                "equals": i
                            }
                        }
                    }
                )
                page_id = self.parent.extensions.parse_page(resp.results[0], get='page_id')
                resp = self.parent.pages.update(page_id=page_id, **{
                    "archived": True
                })
                return resp

    def export_database(self, 
                        database_id: str='', 
                        filter_type: str='name2', 
                        filter_property: str='rich_text', 
                        filter_value: str='', 
                        export_column: list=[''], 
                        format: str='latex'):
        
        filter_dict = self.parent.build.filter3(
            filter_type=filter_type,
            filter_value=filter_value,
            filter_property=filter_property
        )

        resp = self.parent.databases.query(database_id=database_id, **filter_dict)
        report_dict = {}
        key_list = []
        value_list = []
        for i in resp.results:     
            aas = i['properties']
            for key, value in aas.items():
                if key in export_column:
                    value = self.parse_value(value=value)
                    key_list.append(key)
                    value_list.append(value)
                    report_dict[key] = value_list

        for i in range(len(export_column)):
            report_dict[key_list[i]] = value_list[i::len(export_column)]

        sorted_dict = OrderedDict((key, report_dict[key]) for key in export_column)
        
        # df = pandas.DataFrame({'name': ['Raphael', 'Donatello'],'mask': ['red', 'purple'],'weapon': ['sai', 'bo staff']})
        df = pandas.DataFrame(sorted_dict)
        # print(df.to_latex(index=False))
        return df.to_latex(index=False)
    
    def query_relation_page_id(self, database_id, name):
        filter_syntax = [
            ('rich_text', 'name2', 'equals', name),
        ]
        filter_text = self.parent.build.filter(filter_syntax=filter_syntax)
        print(filter_text)

        page = self.parent.databases.query(database_id=database_id, **filter_text).results

        # print(page)
        try:
            return self.parse_page(page=page, get='page_id')
        except Exception as e:
            raise ValueError('未查找到 Page')

