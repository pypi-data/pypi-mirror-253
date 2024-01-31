import pandas as pd
import numpy as np
import re
import json
from datetime import datetime
from apiclient import APIClient, HeaderAuthentication, JsonRequestFormatter
import openai
import os

idToken = None
chartartEndpoint = "https://chartart-app-api-t6dsymrlxq-uc.a.run.app"
userId = None


def create_app(functionClient,name,desc):
  resp = functionClient.post(f"{chartartEndpoint}/apps/", params= {"apiKey" : idToken},  data =
  { "name" : name, "desc" : desc})
  if resp.status_code== 200:
    response_obj = json.loads(resp.content)
  else:
      return {'app_id':''}

  app_id = response_obj['id']
  return {'app_id':app_id}

def setTabView(functionClient,app_id,path):
  resp = functionClient.put(f"{chartartEndpoint}/apps/{app_id}/view/tabs", params = { "apiKey" : idToken,"path" : path}, data = { "showElevation": True,
			"viewType": "tabs"})
  #print(resp)
  return '{'+path+ ' : Set to tab view}. Tabs could be added to '+path+'tabs/}'

def createTab(functionClient,app_id,path,tab_id,tabSeq,tabTitle,query):
  # Set tabbed view
  resp = functionClient.post(endpoint=f"{chartartEndpoint}/apps/{app_id}/tabs/", params = {"apiKey" : idToken, "path" : path } , data = {
				"feedConfig": {
					"default": {
          "dataLocation": f"/posts/{userId}/{app_id}/nlqCharts/chartDocs/{app_id}/posts/data/"+tab_id,
					"query": query
					}
				},
				"id": tab_id,
				"tabSeq": tabSeq,
				"title": tabTitle
		})
  #print(resp)
  return '{Tab '+tab_id+' with path '+path+tab_id+'/ created successfully.}'

def setListView(functionClient,app_id,path):
  if not path == '':
    if not path.endswith('/'):
      path = path+'/'
  resp = functionClient.put(f"{chartartEndpoint}/apps/{app_id}/view/list", params = { "apiKey" : idToken,"path" : path }, data = {
				"mode": "manualPlay",
				"pageSize": 10,
				"pagination": True,
				"postClickSupported": False,
				"showAuthorName": False,
				"showComments": True,
				"showLikeButton": True,
				"showNotebookButton": True,
				"supportsDrilldown": False,
				"drilldownColumns": [],
				"sortCol": [],
				"sortOrder": [],
				"viewType": "list"
	})
  #print(resp)
  return '{List view set for '+path+'}'

def createPieChart(functionClient,app_id,folder_id,chartId,chartTitle,xData,yData,filters):
  resp = functionClient.post(endpoint=f"{chartartEndpoint}/apps/{app_id}/folders/{folder_id}/posts/pie",params = { "apiKey" : idToken}, data = {
						"postType" : "pie",
						"id" : chartId,
						"chartId" : chartId,
            "title" : chartTitle,
            "x" : xData,
            "label" : yData,
           # "scrollableAnnotations" : [ "# Heading 1",  "## Heading 2"],
						"filters" : filters
		})
  #print(resp)
  return '{pie chart '+chartId+' created succesfully.}'

def createCartesianChart(functionClient,app_id,folder_id,chartId,chartTitle,series,xAxisType,xAxisLabel,yAxisLabel ,filters):
  resp = functionClient.post(endpoint=f"{chartartEndpoint}/apps/{app_id}/folders/{folder_id}/posts/cartesian",params = { "apiKey" : idToken}, data = {
						"id" : chartId,
						"chartId" : chartId,
            "title" : chartTitle,
            "series":series,
           # "scrollableAnnotations" : [ "# Heading 1",  "## Heading 2"],
						"filters" : filters,
            #"postType":'cartesian',
            "xAxisType":xAxisType,
            "xAxisLabel":xAxisLabel,
            "yAxisLable":yAxisLabel
		})
  #print(resp)
  return '{cartesian chart '+chartId+ ' created successfully.}'

def setTableView(functionClient,app_id,path,data):
  if not path == '':
    if not path.endswith('/'):
      path = path+'/'

  resp =  functionClient.put(endpoint=f"{chartartEndpoint}/apps/{app_id}/view/table", params = { "apiKey" : idToken, "path" : path }, data = data)
  #print(resp)
  return '{Table view set for '+path+'}'

def createPostsData(functionClient,app_id,folder_id,id,data,filters):
  filters['dateAdded'] = datetime.now().isoformat() + 'Z'
  resp = functionClient.post(endpoint=f"{chartartEndpoint}/apps/{app_id}/folders/{folder_id}/posts/data",params = { "apiKey" : idToken}, data = {
						"data" : data,
						"id" : id,
						"filters" : filters
		})
  return '{data '+id+' added to table}'


functionDict = {
    "create_app":create_app,
    "set_view_tabs": setTabView,
    "set_view_table": setTableView,
    "set_view_list": setListView,
    "create_tabs": createTab,
    "create_posts_pie": createPieChart,
    "create_posts_cartesian": createCartesianChart,
    "create_posts_data": createPostsData
}

splInstructionDict = {
    "create_app": "Come up with a description based on the query if not provided.",
    "set_view_tabs": "Tab view can be set for tabs or drilldowns. For setting view at app level, use empty path: "" For setting for tabs, Use relative 'path' derived from chatHistory. In case of drilldown, add drilldown/ to the end of relative path. for eg if tab view need to be set for sales tab, path is relative_path_of_sales/. In case of drilldown, path will be relative_path_of_sales/drilldown/. Drilldown MUST always end in drilldown/",
    "create_tabs": "New tabs require a 'path' which ends with 'tabs/' where the tab will be created. For a tab in an empty app, set path to 'tabs/'.  'id' and 'path' must not contain spaces. Ensure 'tabSeq' numbers are consecutive at each level, but can restart at new levels. The 'query' parameter in 'feedConfig' defines display criteria (e.g., {'features.customerType': 'paid'} to display charts with paid customerType). Deduce the feedConfig from the userCommand looking for any query condition. Path must always end with 'tabs/'. For eg say new tab 'sales' gets added to analysis tab. path is relative_path_to_analysisTab/tabs/. MAke sure escaping is used in reasoning so that it would not casuse error while json reading",
    "create_posts_pie": "If filters are absent, automatically use the tab's feature query as a filter, Look the query of the tab where charts gets added. strictly follow this rule. Exclude the 'features' prefix in the filter (e.g., use {'price': 'High'} instead of {'features.price': 'High'}). Folder id is absolute last folder and not relative path. Folder id is always the name of the folder",
    "set_view_list": "Determine relative 'path'. Use an empty path ("") for app-level settings and the appropriate relative path for a tab. For eg say a tab tab1 is present at 'tabs/' level. Path will be 'tabs/tab1/'",
    "create_posts_cartesian": "If filters are absent, automatically use the tab's feature query as a filter, Look the query of the tab where charts gets added. strictly follow this rule.  Omit the 'features' prefix in the filter (e.g., {'price': 'High'} instead of {'features.price': 'High'}).Folder id is absolute last folder and not relative path. Folder id is always the name of the folder",
    "set_view_table": "The 'path' should be relative and derived from 'chatHistory'. For setting a table view at the app level, use an empty path (""). For a specific tab, use its relative path. Ensure columns are clearly defined with 'id', 'name', 'type', 'show', and 'description'. 'columnWidthMode' must be set to either 'fill' or a specific width. Include 'canMarkFavourite', 'changeNotificationColumns', and 'drilldownColumns' as needed. 'pagination' should be explicitly set to true or false.",
    "create_posts_data": "Each data post must include a unique 'id' and relevant data fields as specified in the user command.Data must have value for each field of the table columns.id should be different for each entries .Generate a unique data id which is random string. Ensure the 'data' object matches the structure of the tab's columns. Include 'filters' matching the tab level feature key to organize posts. For example if tab has query features.type = xyz, filters will be type:xyz. Validate that all necessary fields are present and correctly formatted. Folder id is absolute last folder and not relative path. Folder id is always the name of the folder and not path "
}

paramExampleDict={

"create_app":[{"role":"user", "content":'\n'+json.dumps({"chatHistory":[],"userCommand":"create a sample app"})},
               {"role":"assistant", "content":'\n'+json.dumps({"reasoning":"In responding to the request for creating a 'sample app', key elements include assigning a name and crafting a description. The name 'sample app' is given. Without a user-provided description, it's necessary to formulate an appropriate one. Thus, 'This is a sample app' is chosen as a concise, relevant description, fulfilling the task's needs while aligning with the app's name","name":"sample app","desc":"This is a sample app"})
               }],
"set_view_tabs":[{
    "role":"user", "content":'\n'+json.dumps({"chatHistory":
                    [{"userCommand": "Create a new app called sample app",
                    "detectedEndpoint": "create_app",
                    "generatedParams": {"name": "sample app",
                    "desc": "This is a sample app"},
                    "apiResponse": {"app_id": "test123"}},
                    {"userCommand": "add new tab tab1",
                    "detectedEndpoint": "create_tabs",
                    "generatedParams": {"path": "tabs/","id": "tab1"},
                    "apiResponse": "Response 200"}],
                    "userCommand":"set view as tabs",})},
    {"role":"assistant", "content":'\n'+json.dumps({"reasoning":"The assistant's task is to set the view for a specific tab in an app. The required 'app_id' is obtained from the chatHistory, identified as 'test123' from a previous app creation command. For the 'path', the user's command to 'add new tab tab1' is crucial. This command indicates the need to focus on this specific tab. Hence, the path is determined to be 'tabs/tab1/', aligning with the user's intention to set the view for 'tab1' within the app.","app_id": "test123", "path":"tabs/tab1/"})},
      {"role":"user", "content":'\n'+json.dumps({"chatHistory":
                    [{"userCommand": "Create a new app called sample app",
                    "detectedEndpoint": "create_app",
                    "generatedParams": {"name": "sample app",
                    "desc": "This is a sample app"},
                    "apiResponse": {"app_id": "test123"}}],"userCommand":"set view as tabs"})},
    {"role":"assistant", "content":'\n'+json.dumps({"reasoning":"In this task, the assistant is required to set the view of an entire app as tabs. From the chatHistory, the 'app_id' is extracted as 'test123', relating to the app in question. The user's command 'set view as tabs' suggests a general application-wide setting, not limited to a specific tab. Therefore, the 'path' should be empty. This indicates that the view setting is to be applied at the app level, encompassing all aspects of the app, rather than targeting a specific tab or component.","app_id": "test123", "path":""})},
               ],
"set_view_list":[{ "role":"user", "content":'\n'+json.dumps({"chatHistory":
                    [{"userCommand": "Create a new app called sample app",
                    "detectedEndpoint": "create_app",
                    "generatedParams": {"name": "sample app",
                    "desc": "This is a sample app"},
                    "apiResponse": {"app_id": "test123"}},
                    {"userCommand": "add new tab tab1",
                    "detectedEndpoint": "create_tabs",
                    "generatedParams": {"path": "tabs/",
                    "id": "tab1"},
                    "apiResponse": {"app_id": "test123"}}],
                    "userCommand":"set view as list"})},
    {"role":"assistant", "content":'\n'+json.dumps({"reasoning":"In this scenario, the assistant's task is to set the view of a specific tab within an app to a list format. The 'app_id' is readily available from the chatHistory as 'test123', linked to the app created earlier. The user's latest command involves setting the view as a list, but it doesn't specify which tab. The most recent tab interaction in the chatHistory is with 'tab1', which was added in the previous command. It is logical to infer that the user intends to apply the list view to this tab. Therefore, the path is constructed as 'tabs/tab1/', indicating that the list view setting is for 'tab1' within the app. This alignment of the path with the most recent tab-related activity in the chatHistory ensures that the assistant's response is contextually relevant and accurate","app_id": "test123", "path":"tabs/tab1/"})}],


"set_view_table": [
    {
      "role": "user",
      "content": "\n{\"chatHistory\": [{\"userCommand\": \"Create a new app called sample app\", \"detectedEndpoint\": \"create_app\", \"generatedParams\": {\"name\": \"sample app\", \"desc\": \"This is a sample app\"}, \"response\": {\"app_id\": \"test123\"}}, {\"userCommand\": \"add new tab tab1\", \"detectedEndpoint\": \"create_tabs\", \"generatedParams\": {\"path\": \"tabs/\", \"id\": \"tab1\"}, \"response\": {\"app_id\": \"test123\"}}], \"userCommand\": \"set view as table with two columns customer and sales and drilldown on customer\"}"
    },
    {
        "role": "assistant",
        "content": "\n{\"reasoning\": \"To configure the 'tab1' tab as a table view, specify columns for 'Customer' and 'Total Sales (Lakhs)' with drilldown enabled on the 'Customer' column. Additional features like pagination and search bar are included for enhanced functionality.\", \"app_id\": \"test123\", \"path\": \"tabs/tab1/\", \"tableConfig\": {\"canMarkFavourite\": False, \"changeNotificationColumns\": [\"customer\"], \"columnWidthMode\": \"fill\", \"columns\": [{\"flex\": 2, \"id\": \"customer\", \"name\": \"Customer\", \"show\": True, \"type\": \"text\", \"description\": \"Customer Name\"}, {\"flex\": 2, \"id\": \"sales\", \"name\": \"Total Sales (Lakhs)\", \"show\": True, \"type\": \"number\", \"description\": \"Total sales so far\"}], \"drilldownColumns\": [\"customer\"], \"frozenColumnsCount\": 1, \"searchBarEmptyText\": \"Search company e.g. ABC Pvt Ltd (not yet working)\", \"pageSize\": 300, \"pagination\": True, \"rowSub\": \"\", \"searchIndexField\": \"data.customer\", \"searchIndexId\": \"customers\", \"showSearchBar\": True, \"sortCol\": [], \"sortOrder\": [], \"supportsDrilldown\": True}}"
    }
],
"create_posts_data": [
    {

      "role": "user",
      "content": "\n{\"chatHistory\": [{\"userCommand\": \"Create a new app called sample app\", \"detectedEndpoint\": \"create_app\", \"generatedParams\": {\"name\": \"sample app\", \"desc\": \"This is a sample app\"}, \"response\": {\"app_id\": \"test123\"}}, {\"userCommand\": \"add new tab tab1\", \"detectedEndpoint\": \"create_tabs\", \"generatedParams\": {\"path\": \"tabs/\", \"id\": \"tab1\"}, \"response\": {\"app_id\": \"test123\"}}], \"userCommand\": \"Add sales data to the tab1 with each row containing 'Customer/Vendor Name' and 'Total Amount'.\"}"

    },
    {
        "role": "assistant",
        "content": "\n{\"reasoning\": \"To populate the 'customers' tab with sales data, each data post will include 'Customer/Vendor Name' and 'Total Amount'. Unique IDs will be assigned to each post along with an order index for sorting.Lets detect the folder id as well as filter corresponding to table setting. Since folder id is absolute and not a path, it is tab1 .Data must have id as well as filter\", \"app_id\": \"test123\",\"folder_id\":\"tab1\", \"data\": {\"customer\": \"Customer/Vendor Name\", \"sales\": \"Total Amount\"}, \"id\": \"amountId123\", \"filters\": {\"type\": \"row\", \"order\": \"incremental_order\"}}"
    }
],

"create_tabs":[{ "role":"user", "content":'\n'+json.dumps({"chatHistory":
                    [{"userCommand": "Create a new app called sample app",
                    "detectedEndpoint": "create_app",
                    "generatedParams": {"name": "sample app",
                    "desc": "This is a sample app"},
                    "apiResponse": {"app_id": "test123"}},
                    {"userCommand": "set view tab ",
                    "detectedEndpoint": "set_view_tabs",
                    "generatedParams": {"app_id": "test123","path": ""},
                    "apiResponse": None},
                    {"userCommand": "Create a new tab 'sales' which will show charts with feature type = charts",
                    "detectedEndpoint": "create_tabs",
                    "params": {"app_id": "test123","path": "tabs/","id": "sales","tabSeq": 1,"title": "Sales",
                              "feedConfig": {"query": {"features.type": "charts"}}},"apiResponse": None},
                    {"userCommand": "set tab view for the tab","detectedEndpoint": "set_view_list",
                    "generatedParams": {"app_id": "test123", "path": "tabs/sales/"},"apiResponse": "<Response [200]>"}],
                    "userCommand":"create a new tab company growth which shows charts with type growth"})},
                {"role":"assistant", "content":'\n'+json.dumps({"reasoning":"In this task, we need to create a new tab within an sales tab, requiring parameters like app_id, path, id, tabSeq, title, and feedConfig. The app_id is already known from the chatHistory as 'test123', which is associated with the previously created app. Ensuring path always ends with '/tabs'.The 'path' for a new tab at the sales tab level should be 'tabs/sales/tabs/'. For the 'id', since the tab is named 'company growth', a suitable ID without spaces is 'company_growth'. The 'tabSeq' indicates the order of the tab; as this is the second tab being created at the app level, 'tabSeq' is set to 2. The 'title' of the tab is derived from the user command, set as 'Company Sales'. Finally, for 'feedConfig', the focus is on displaying charts with a feature type of 'growth'. So let us deduce the query, Hence query will have 'features.type:growth'.",
                        "app_id": "test123","path": "tabs/sales/tabs/",
                        "addSearchBar": False,"id": "company_growth","tabSeq": 2,"title": "Company Sales",
                        "feedConfig": {"query": {"features.type":"growth"}}})}],
"create_posts_pie":[{ "role":"user", "content":'\n'+json.dumps({"chatHistory":
                    [{"userCommand": "Create a sample app",
                      "detectedEndpoint": "create_app",
                      "generatedParams": {"name": "sample app","desc": "This is a sample app"},"apiResponse": {"app_id": "test123"}},
                    {"userCommand": "Create a new tab 'sales' which will show charts with feature type = charts",
                    "detectedEndpoint": "create_tabs",
                    "generatedParams": {"app_id": "test123","path": "tabs/","id": "sales","tabSeq": 1,"title": "Sales",
                              "feedConfig": {"query": {"features.type": "charts"}}},"apiResponse": None},
                    {"userCommand": "set list view for the tab","detectedEndpoint": "set_view_list",
                    "generatedParams": {"app_id": "test123", "path": "tabs/sales/"},"apiResponse": "<Response [200]>"}],
                    "userCommand":"Add a sample pie chart of two country and its population"})},
                    {"role":"assistant", "content":'\n'+json.dumps({"reasoning":"In this task, the assistant is asked to add a sample pie chart to the app. The 'app_id' is known from the chatHistory as 'test123', associated with the previously created 'sample app'. The most relevant tab for adding a pie chart is 'sales', as indicated by the user's earlier command to create this tab for displaying charts. Therefore, the 'folder_id' for the pie chart is deduced as 'sales', aligning with the ID of the tab where the chart is to be displayed. Since the 'sales' tab was previously set to show charts (feature type = charts), the pie chart should also align with this theme. Hence, filters are set to 'type: charts'. The chart's ID and title are formulated to be descriptive of its content – 'samplePieChart' and 'Population Pie Chart', respectively. Finally, to fulfill the user's request for a sample pie chart, sample data representing the populations of two countries, India and China, is generated to create the chart making sure two x and label values are generated",
                    "app_id": "test123",
                    "folder_id": "sales",
                    "id": "samplePieChart","postType": "pie",
                    "filters": {"type" : "charts"},"chartId": "samplePieChart","title": "Population Pie Chart",
                    "scrollableAnnotations": None,
                    "x": [152773, 267383],
                    "label": ["India", "China"]})}],
"create_posts_cartesian":[{ "role":"user", "content":'\n'+json.dumps({"chatHistory":
                    [{"userCommand": "Create a sample app",
                      "apiEndpoint": "create_app",
                      "params": {"name": "sample app","desc": "This is a sample app"},"response": {"app_id": "test123"}},
                    {"userCommand": "Create a new tab 'sales' which will show charts with feature type = charts",
                    "apiEndpoint": "create_tabs",
                    "params": {"app_id": "test123","path": "tabs/","id": "sales","tabSeq": 1,"title": "Sales",
                              "feedConfig": {"query": {"features.type": "charts"}}},"response": None},
                    {"userCommand": "set list view for the tab","apiEndpoint": "set_view_list",
                    "params": {"app_id": "test123", "path": "tabs/sales/"},"response": "<Response [200]>"}],
                    "userCommand":"Add a sample line chart of Country population over two years"})},
                    {"role":"assistant", "content":'\n'+json.dumps({"reasoning":"The assistant's task is to add a line chart to a specific tab in the app. From the chatHistory, the 'app_id' 'test123' is identified, linked to the previously created 'sample app'. The user's request to add a line chart specifying 'Country population over two years' guides the choice of chart type and data. The target tab for this chart is 'sales', as it was recently created to display charts. Therefore, the 'folder_id' for the line chart is determined to be 'sales', aligning with the tab's ID. Since the 'sales' tab is designed to feature charts, the filter is set to 'type: charts' to maintain consistency with the tab's theme. The ID and title of the chart are chosen to reflect its content and purpose: 'sampleLineChart' and 'Population Line Chart', respectively.Analyzing the schema, We need to generate a series with x, y and label.Make sure these parameters are within series.To visualize the population data over two years, a series with bar type is used, representing the years 2019 and 2020 along the x-axis and the corresponding population figures on the y-axis. The x-axis is labeled 'Year' and the y-axis 'Total Population', with the x-axis type set to 'categorical' to suit the data representation",
                    "app_id": "test123",
                    "folder_id": "sales",
                    "id": "samplePieChart","postType": "cartesian",
                    "filters": {"type" : "charts"},"chartId": "sampleLineChart","title": "Population Line Chart",
                    "scrollableAnnotations": None,
                    "series" : [
							                  {"type" : "line",
								                "x" : [2019,2020],
								                "y" : [1672672,7267272],
								                "labels": 'Total Amount'}],
						        "xAxisLabel" : 'Year',
						        "yAxisLabel" : 'Total Population',
						        "xAxisType" : "categorical",
                   })}],

}


schemaDict = {
"create_app": json.dumps({
  "post": {
    "summary": "Create App",
    "description": "Create a new application specified with name and description.",
    "requestBody": {
      "required": True,
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/AppCreate"
          }
        }
      }
    }
  },
  "schemas": {
    "AppCreate": {
      "type": "object",
      "required": ["name", "desc"],
      "properties": {
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Name of the App. Displayed on login page and in banner on top after login"
        },
        "desc": {
          "type": "string",
          "title": "Desc",
          "description": "A longer description of the App. Displayed below the name of app on login page only."
        }
      },
      "title": "AppCreate"
    }
  }
}
),

"set_view_tabs" : json.dumps({
  "put": {
    "summary": "Set View",
    "description": "Set the view as 'tab' of the entity specified by the path query parameter.",
    "operationId": "set_view_tabs",
    "parameters": [
      {
        "name": "app_id",
        "in": "path",
        "required": True,
        "schema": {
          "type": "string",
          "title": "App Id"
        }
      },
      {
        "name": "path",
        "in": "query",
        "required": True,
        "description": "Path to the entity for which the view is to be set of type 'tab'. e.g. tabs/customers/, tabs/customers/drilldown/tabs/customer_charts/",
        "schema": {
          "type": "string",
          "title": "Path"
        }
      }
    ],
    "requestBody": {
      "required": True,
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/TabViewConfig-Input"
          }
        }
      }
    }
  },
  "schemas": {
    "TabViewConfig-Input": {
      "type": "object",
      "required": ["viewType"],
      "properties": {
        "showElevation": {
          "anyOf": [{"type": "boolean"}, {"type": "null"}],
          "title": "Showelevation",
          "default": False
        },
        "viewType": {
          "const": "tabs",
          "title": "Viewtype"
        },
        "tabs": {
          "anyOf": [
            {
              "type": "array",
              "items": {"$ref": "#/components/schemas/Tab"}
            },
            {
              "type": "null"
            }
          ],
          "title": "Tabs",
          "hidden": True
        }
      },
      "title": "TabViewConfig"
    }
  }
}
),

"set_view_table": json.dumps({
    "put": {
      "summary": "Set View",
      "description": "Set the view as 'table' of the entity specified by the path query parameter.",
      "operationId": "set_view_table",
      "parameters": [
        {
          "name": "app_id",
          "in": "path",
          "required": True,
          "schema": {
            "type": "string",
            "title": "App Id"
          }
        },
        {
          "name": "path",
          "in": "query",
          "required": True,
          "schema": {
            "type": "string",
            "description": "Path to the entity for which the view is to be set of type 'table'. e.g. tabs/customers/, tabs/customers/drilldown/tabs/customer_charts/",
            "title": "Path"
          },
          "description": "Path to the entity for which the view is to be set of type 'table'. e.g. tabs/customers/, tabs/customers/drilldown/tabs/customer_charts/"
        }
      ],
      "requestBody": {
        "required": True,
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/TableViewConfig"
            }
          }
        }
      }
    }
  ,
  "schemas": {
    "TableViewConfig": {
      "type": "object",
      "required": ["viewType", "canMarkFavourite", "columns"],
      "properties": {
        "viewType": {
          "const": "table",
          "title": "Viewtype"
        },
        "canMarkFavourite": {
          "type": "boolean",
          "title": "Canmarkfavourite"
        },
        "changeNotificationColumns": {
          "anyOf": [
            {
              "type": "array",
              "items": {
                "type": "string"
              }
            },
            {
              "type": "null"
            }
          ],
          "title": "Changenotificationcolumns"
        },
        "columnWidthMode": {
          "anyOf": [
            {
              "type": "string"
            },
            {
              "type": "null"
            }
          ],
          "title": "Columnwidthmode"
        },
        "columns": {
          "type": "array",
          "items": {
            "$ref": "#/components/schemas/TableViewColumn"
          },
          "title": "Columns"
        },
        "drilldownColumns": {
          "anyOf": [
            {
              "type": "array",
              "items": {
                "type": "string"
              }
            },
            {
              "type": "null"
            }
          ],
          "title": "Drilldowncolumns"
        },
        "frozenColumnsCount": {
          "anyOf": [
            {
              "type": "integer"
            },
            {
              "type": "null"
            }
          ],
          "title": "Frozencolumnscount"
        },
        "searchBarEmptyText": {
          "anyOf": [
            {
              "type": "string"
            },
            {
              "type": "null"
            }
          ],
          "title": "Searchbaremptytext"
        },
        "pageSize": {
          "anyOf": [
            {
              "type": "integer"
            },
            {
              "type": "null"
            }
          ],
          "title": "Pagesize"
        },
        "pagination": {
          "anyOf": [
            {
              "type": "boolean"
            },
            {
              "type": "null"
            }
          ],
          "title": "Pagination"
        },
        "rowSub": {
          "anyOf": [
            {
              "type": "string"
            },
            {
              "type": "null"
            }
          ],
          "title": "Rowsub"
        },
        "searchIndexField": {
          "anyOf": [
            {
              "type": "string"
            },
            {
              "type": "null"
            }
          ],
          "title": "Searchindexfield"
        },
        "searchIndexId": {
          "anyOf": [
            {
              "type": "string"
            },
            {
              "type": "null"
            }
          ],
          "title": "Searchindexid"
        },
        "showSearchBar": {
          "anyOf": [
            {
              "type": "boolean"
            },
            {
              "type": "null"
            }
          ],
          "title": "Showsearchbar",
          "default": False
        },
        "sortCol": {
          "anyOf": [
            {
              "type": "array",
              "items": {
                "type": "string"
              }
            },
            {
              "type": "null"
            }
          ],
          "title": "Sortcol"
        },
        "sortOrder": {
          "anyOf": [
            {
              "type": "array",
              "items": {
                "type": "string"
              }
            },
            {
              "type": "null"
            }
          ],
          "title": "Sortorder"
        },
        "supportsDrilldown": {
          "anyOf": [
            {
              "type": "boolean"
            },
            {
              "type": "null"
            }
          ],
          "title": "Supportsdrilldown",
          "default": False
        }
      },
      "title": "TableViewConfig"
    },
    "TableViewColumn": {
      "type": "object",
      "required": ["id", "type"],
      "properties": {
        "id": {
          "type": "string",
          "title": "Id"
        },
        "name": {
          "anyOf": [
            {
              "type": "string"
            },
            {
              "type": "null"
            }
          ],
          "title": "Name"
        },
        "show": {
          "anyOf": [
            {
              "type": "boolean"
            },
            {
              "type": "null"
            }
          ],
          "title": "Show",
          "default": True
        },
        "type": {
          "type": "string",
          "title": "Type"
        },
        "description": {
          "anyOf": [
            {
              "type": "string"
            },
            {
              "type": "null"
            }
          ],
          "title": "Description"
        }
      },
      "title": "TableViewColumn"
    }
  }}
)
,

"set_view_list": json.dumps({
  "put": {
    "summary": "Set View",
    "description": "Set the view as 'list' of the entity specified by the path query parameter.",
    "operationId": "set_view_list",
    "parameters": [
      {
        "name": "app_id",
        "in": "path",
        "required": True,
        "schema": {
          "type": "string",
          "title": "App Id"
        }
      },
      {
        "name": "path",
        "in": "query",
        "required": True,
        "description": "Path to the entity for which the view is to be set of type 'list'. e.g. tabs/customers/, tabs/customers/drilldown/tabs/customer_charts/",
        "schema": {
          "type": "string",
          "title": "Path"
        }
      }
    ],
    "requestBody": {
      "required": True,
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/ListViewConfig"
          }
        }
      }
    }
  },
  "schemas": {
    "ListViewConfig": {
      "type": "object",
      "required": [
        "viewType",
        "mode",
        "pageSize",
        "pagination",
        "postClickSupported",
        "showAuthorName",
        "showComments",
        "showLikeButton",
        "showNotebookButton",
        "sortCol",
        "sortOrder"
      ],
      "properties": {
        "viewType": {
          "const": "list",
          "title": "Viewtype"
        },
        "mode": {
          "type": "string",
          "title": "Mode"
        },
        "pageSize": {
          "type": "integer",
          "title": "Pagesize"
        },
        "pagination": {
          "type": "boolean",
          "title": "Pagination"
        },
        "postClickSupported": {
          "type": "boolean",
          "title": "Postclicksupported"
        },
        "showAuthorName": {
          "type": "boolean",
          "title": "Showauthorname"
        },
        "showComments": {
          "type": "boolean",
          "title": "Showcomments"
        },
        "showLikeButton": {
          "type": "boolean",
          "title": "Showlikebutton"
        },
        "showNotebookButton": {
          "type": "boolean",
          "title": "Shownotebookbutton"
        },
        "sortCol": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "title": "Sortcol"
        },
        "sortOrder": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "title": "Sortorder"
        }
      },
      "title": "ListViewConfig"
    }
  }
}
) ,

"create_tabs":json.dumps({
  "post": {
    "summary": "Create Tab",
    "description": "Add a tab under the path specified by the path query parameter.",
    "operationId": "create_tabs",
    "parameters": [
      {
        "name": "app_id",
        "in": "path",
        "required": True,
        "schema": {
          "type": "string",
          "title": "App Id"
        }
      },
      {
        "name": "path",
        "in": "query",
        "required": True,
        "description": "Path to the entity for which the view is to be set. Follows a hierarchical notation. e.g. tabs/customers/, tabs/customers/drilldown/tabs/customer_charts/",
        "schema": {
          "type": "string",
          "title": "Path"
        }
      }
    ],
    "requestBody": {
      "required": True,
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/Tab"
          }
        }
      }
    }
  },
  "schemas": {
    "Tab": {
      "type": "object",
      "required": ["id", "tabSeq", "title","feedConfig"],
      "properties": {
        "addSearchBar": {
          "anyOf": [{"type": "boolean"}, {"type": "null"}],
          "title": "Addsearchbar",
          "default": False
        },
        "id": {
          "type": "string",
          "title": "Id"
        },
        "tabSeq": {
          "type": "integer",
          "title": "Tabseq"
        },
        "title": {
          "type": "string",
          "title": "Title"
        },
        "feedConfig": {
          "anyOf": [
            {
              "type": "object",
              "additionalProperties": {
                "$ref": "#/components/schemas/Feed"
              }
            },
            {
              "type": "null"
            }
          ],
          "title": "Feedconfig"
        }
      },
      "title": "Tab"
    },
    "Feed": {
      "type": "object",
      "properties": {
        "dataLocation": {
          "anyOf": [{"type": "string"}, {"type": "null"}],
          "title": "Datalocation"
        },
        "query": {
          "anyOf": [{"type": "object"}, {"type": "null"}],
          "title": "Query"
        },
        "feed": {
          "anyOf": [{"type": "string"}, {"type": "null"}],
          "title": "Feed"
        }
      },
      "title": "Feed"
    }
  }
}
),

"create_posts_pie":  json.dumps({"post":{
  "summary": "Create Chart",
  "description": "Adds a pie chart under the folder specified by folder_id.",
  "operationId": "create_posts_pie",
  "parameters": [
    {
      "name": "app_id",
      "in": "path",
      "required": True,
      "schema": {
        "type": "string",
        "title": "App Id"
      }
    },
    {
      "name": "folder_id",
      "in": "path",
      "required": True,
      "schema": {
        "type": "string",
        "title": "Folder Id"
      }
    },
    {
      "name": "id",
      "in": "query",
      "required": True,
      "schema": {
        "type": "string",
        "description": "Unique identifier for the post"
      }
    },
    {
      "name": "postType",
      "in": "query",
      "required": True,
      "schema": {
        "type": "string",
        "default": "pie",
        "description": "Must be set to 'pie'"
      }
    },
    {
      "name": "filters",
      "in": "query",
      "required": True,
      "schema": {
        "type": ["object", "null"],
        "description": "Filters"
      }
    },
    {
      "name": "chartId",
      "in": "query",
      "required": True,
      "schema": {
        "type": "string",
        "description": "Unique identifier for the chart"
      }
    },
    {
      "name": "title",
      "in": "query",
      "required": True,
      "schema": {
        "type": "string",
        "description": "Title for the chart."
      }
    },
    {
      "name": "scrollableAnnotations",
      "in": "query",
      "required": False,
      "schema": {
        "type": ["array", "null"],
        "items": {
          "type": "string"
        },
        "description": "Array of markdown text annotations to be displayed alongside the chart."
      }
    },
    {
      "name": "x",
      "in": "query",
      "required": True,
      "schema": {
        "type": "array",
        "items": {
          "type": "number"
        },
        "description": "Denoting the size of each pie. Must include the full data as an array."
      }
    },
    {
      "name": "label",
      "in": "query",
      "required": True,
      "schema": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "Label for each slice of the pie. Must include the full data as an array."
      }
    }
  ]
}})
,

"create_posts_cartesian":json.dumps({
  "post": {
    "summary": "Create Chart",
    "description": "Adds a cartesian chart under the folder specified by folder_id.",
    "operationId": "create_posts_cartesian",
    "parameters": [
      {
        "name": "app_id",
        "in": "path",
        "required": True,
        "schema": {
          "type": "string",
          "title": "App Id"
        }
      },
      {
        "name": "folder_id",
        "in": "path",
        "required": True,
        "schema": {
          "type": "string",
          "title": "Folder Id"
        }
      }
    ],
    "requestBody": {
      "required": True,
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/CartesianChart"
          }
        }
      }
    }
  },
  "schemas": {
    "CartesianChart": {
      "type": "object",
      "required": ["xAxisType", "postType", "id", "chartId", "title"],
      "properties": {
        "xAxisLabel": {
          "anyOf": [{"type": "string"}, {"type": "null"}],
          "title": "Xaxislabel",
          "description": "Label for x axis"
        },
        "yAxisLabel": {
          "anyOf": [{"type": "string"}, {"type": "null"}],
          "title": "Yaxislabel",
          "description": "Label for y axis"
        },
        "xAxisType": {
          "type": "string",
          "title": "Xaxistype",
          "description": "One of numeric, datetime, category"
        },
        "yAxisMinimum": {
          "anyOf": [{"type": "number"}, {"type": "null"}],
          "title": "Yaxisminimum",
          "description": "Minimum value of y axis scale"
        },
        "yAxisMaximum": {
          "anyOf": [{"type": "number"}, {"type": "null"}],
          "title": "Yaxismaximum",
          "description": "Maximum value of y axis scale"
        },
        "xAxisDateFormat": {
          "anyOf": [{"type": "string"}, {"type": "null"}],
          "title": "Xaxisdateformat",
          "description": "If axis is datetime then the format in which date/time is to be displayed. Any pattern supported by Dart language DateFormat class is allowed."
        },
        "id": {
          "type": "string",
          "title": "Id",
          "description": "Unique identifier for the post"
        },
        "postType": {
          "const": "cartesian",
          "title": "Posttype",
          "description": "Must be set to 'cartesian'",
          "default": "cartesian"
        },
        "filters": {
          "anyOf": [{"type": "object"}, {"type": "null"}],
          "title": "Filters"
        },
        "chartId": {
          "type": "string",
          "title": "Chartid",
          "description": "Unique identifier for the chart"
        },
        "title": {
          "type": "string",
          "title": "Title",
          "description": "Title for the chart."
        },
        "scrollableAnnotations": {
          "anyOf": [{"type": "array", "items": {"type": "string"}}, {"type": "null"}],
          "title": "Scrollableannotations",
          "description": "Array of markdown text annotations to be displayed alongside the chart."
        },
        "series": {
          "type": "array",
          "items": {
            "anyOf": [{"$ref": "#/components/schemas/BarSeries"}, {"$ref": "#/components/schemas/LineSeries"}]
          },
          "title": "Series",
          "description": "Array of series to be plotted"
        }
      },
      "title": "CartesianChart"
    },
    "BarSeries": {
      "type": "object",
      "required": ["type", "x", "y"],
      "properties": {
        "type": {
          "const": "bar",
          "title": "Type",
          "description": "Can be one of bar, column, stackedBar"
        },
        "x": {
          "type": "array",
          "items": {
            "anyOf": [
              {"type": "number"},
              {"type": "string"},
              {"type": "string", "format": "date-time"}
            ]
          },
          "title": "X",
          "description": "Data for the X-axis. Can be a number, string, or date. Must include the full data as an array"
        },
        "y": {
          "type": "array",
          "items": {"type": "number"},
          "title": "Y",
          "description": "Numeric data for the Y-axis. Must include the full data as an array"
        },
        "c": {
          "anyOf": [{"type": "string"}, {"type": "null"}],
          "title": "C",
          "description": "Color of the line. Can be a hex code or color name."
        },
        "labels": {
          "anyOf": [{"type": "string"}, {"type": "null"}],
          "title": "Labels",
          "description": "Label for the series. If not specify will be auto constructed."
        },
        "xAxisName": {
          "anyOf": [{"type": "string"}, {"type": "null"}],
          "title": "Xaxisname",
          "description": "On which x axis is series is to be plotted. Required only in multi axis charts.",
          "default": "None"
        },
        "yAxisName": {
          "anyOf": [{"type": "string"}, {"type": "null"}],
          "title": "Yaxisname",
          "description": "On which y axis is series is to be plotted. Required only in multi axis charts.",
          "default": "None"
        },
        "barType": {
          "anyOf": [{"$ref": "#/components/schemas/BarTypeEnum"}, {"type": "null"}],
          "default": "bar"
        }
      },
      "title": "BarSeries"
    },
    "BarTypeEnum": {
      "type": "string",
      "enum": ["bar", "column", "stackedBar", "stackedColumn", "stackedBar100", "stackedColumn100"],
      "title": "BarTypeEnum"
    },
    "LineSeries": {
      "type": "object",
      "required": ["type", "x", "y"],
      "properties": {
        "type": {
          "const": "line",
          "title": "Type",
          "description": "Can be one of line, area, spline"
        },
        "x": {
          "type": "array",
          "items": {
            "anyOf": [
              {"type": "number"},
              {"type": "string"},
              {"type": "string", "format": "date-time"}
            ]
          },
          "title": "X",
          "description": "Data for the X-axis. Can be a number, string, or date. Must include the full data as an array"
        },
        "y": {
          "type": "array",
          "items": {"type": "number"},
          "title": "Y",
          "description": "Numeric data for the Y-axis. Must include the full data as an array"
        },
        "c": {
          "anyOf": [{"type": "string"}, {"type": "null"}],
          "title": "C",
          "description": "Color of the line. Can be a hex code or color name."
        },
        "labels": {
          "anyOf": [{"type": "string"}, {"type": "null"}],
          "title": "Labels",
          "description": "Label for the series. If not specify will be auto constructed."
        },
        "xAxisName": {
          "anyOf": [{"type": "string"}, {"type": "null"}],
          "title": "Xaxisname",
          "description": "On which x axis is series is to be plotted. Required only in multi axis charts.",
          "default": "None"
        },
        "yAxisName": {
          "anyOf": [{"type": "string"}, {"type": "null"}],
          "title": "Yaxisname",
          "description": "On which y axis is series is to be plotted. Required only in multi axis charts.",
          "default": "None"
        },
        "lineType": {
          "anyOf": [{"$ref": "#/components/schemas/LineTypeEnum"}, {"type": "null"}],
          "default": "line"
        }
      },
      "title": "LineSeries"
    },
    "LineTypeEnum": {
      "type": "string",
      "enum": ["line", "area", "spline", "stepLine", "splineArea", "stepArea", "stackedLine", "stackedArea", "stackedArea100", "stackedLine100"],
      "title": "LineTypeEnum"
    }
  }
}
),
"create_posts_data":json.dumps({
  "post": {
    "summary": "Create Chart",
    "description": "Adds data which is in the form of a dictionary (rows/columns) to the folder specified by folder_id. This data can then be displayed in a table view.",
    "operationId": "create_posts_data",
    "parameters": [
      {
        "name": "app_id",
        "in": "path",
        "required": True,
        "schema": {
          "type": "string",
          "title": "App Id"
        }
      },
      {
        "name": "folder_id",
        "in": "path",
        "required": True,
        "schema": {
          "type": "string",
          "title": "Folder Id"
        }
      }
    ],
    "requestBody": {
      "required": True,
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/PostData"
          }
        }
      }
    }
  },
  "schemas": {
    "PostData": {
      "type": "object",
      "required": [
        "id",
        "data",
        "filters"
      ],
      "properties": {
        "id": {
          "type": "string",
          "title": "Id",
          "description": "Unique identifier for the post"
        },
        "postType": {
          "const": "data",
          "title": "Posttype",
          "description": "Must be set to 'data'",
          "default": "data"
        },
        "filters": {
          "anyOf": [
            {
              "type": "object"
            },
            {
              "type": "null"
            }
          ],
          "title": "Filters"
        },
        "data": {
          "type": "object",
          "title": "Data",
          "description": "A dictionary of data which can be be displayed in a table with rows and columns."
        }
      },
      "title": "PostData"
    }
  }
}
)
}


class appBuilder:
    def __init__(self):
        # Stores endpoints and their associated data
        self.endpoints = {}
        self.chatHistory = []
        self.generalInstruction="\nYou are a system which derives relevant parameters from user query which would facilitate an app-building system offering three distinct views. In the List View, users can view and interact with charts. The Tab View allows the addition of multiple tabs, each capable of hosting its own List, Tab, or Table view, facilitating versatile content organization. Finally, the Table View provides a detailed data presentation format, complete with drilldown features for in-depth analysis."
        self.functionClient = APIClient(
   				request_formatter=JsonRequestFormatter
   				)
        self.llmClient = None
        

    def setCredentials(self,api_key,id_Token,user_Id):
        self.llmClient = openai.OpenAI(
  		  api_key=api_key,
  		  base_url='https://api.together.xyz')
        global userId
        global idToken
        userId = user_Id
        idToken = id_Token
        endpointDict = {
            "create_app": "Use this endpoint when the command is to create a new application.",
            "set_view_tabs": "Choose this when the command involves setting the user interface to display tabs or drilldown.",
            "set_view_table": "Choose this wwhen the command involves setting the user interface to display table",
            "set_view_list": "This is used when the command is to set the user interface to a list view.",
            "create_tabs": "Select this endpoint for commands related to adding new tabs in the interface.",
            "create_posts_pie": "Use this for commands asking to add a pie chart to either a tab or a list view.",
            "create_posts_cartesian": "This endpoint is for commands that involve adding a cartesian chart, like a line or bar chart, to a tab or list.",
            "create_posts_data": "This endpount is for commands that involve adding table related data.",

          }

        for endpoint,description in endpointDict.items():
            self.register_endpoint(endpoint,description,schemaDict[endpoint],splInstructionDict[endpoint],paramExampleDict[endpoint],functionDict[endpoint])
    
    def extract_json_response(self,text):
        json_pattern = r'(\{.*?\})'
        matches = re.findall(json_pattern, text, re.DOTALL)
        if matches:
            json_str = matches[-1]
            try:
                return json.loads(json_str)
            except json.JSONDecodeError:
                return eval(json_str)
        else:
            return None

    def formatFolder(self,folder_id):
      folder_id = folder_id.replace('tabs/','')
      if folder_id.endswith('/'):
        folder_id = folder_id[:-1]
      folder_id = folder_id.split('/')[-1]
      return folder_id

    def callLLM(self,messageList,max_tokens=2048):
      chat_completion = self.llmClient.chat.completions.create(
          messages=messageList,
          #model="mistralai/Mixtral-8x7B-Instruct-v0.1",
          model="NousResearch/Nous-Hermes-2-Mixtral-8x7B-DPO",
          #model="NousResearch/Nous-Hermes-2-Mixtral-8x7B-SFT",
          max_tokens=max_tokens,
          #stop=[' ','\n']
        )
      response = chat_completion.choices[0].message.content
      return response

    def create_classification_prompt(self,endpoints):
      prompt = "\nAs an AI classification assistant, your task is to analyze user commands and accurately classify them into one of the specified API endpoints. Each endpoint corresponds to a specific function.\n\n"
      for name,endpoint in endpoints.items():
          description = endpoint.get('description', 'No description provided.')
          endpoint_name = endpoint.get('endpoint', None)
          prompt += f'- "{endpoint_name}": {description}\n'
      prompt += "\nYour response should be in JSON format, clearly specifying the selected endpoint based on the user's command. The format should be: {\"apiCall\": \"selected_endpoint\"}. If a user command does not match any of the specified endpoints, classify it as out of scope and return {\"apiCall\": None}.\n\nRemember, your response must only include the JSON output, with no additional explanations or text.\n\nEndpoints can include a variety of functions, and it is your responsibility to determine the most appropriate endpoint for each user command."
      return prompt

    def register_endpoint(self, endpoint_name, description,schema=None,splInstruction=None,exampleList=[],function=None):
        self.endpoints[endpoint_name] = {
            "endpoint" : endpoint_name,
            "description": description,
            "schema":schema,
            "function":function,
            "splInstruction":splInstruction,
            "exampleList":exampleList
        }


    def classifyEndpoint(self,user_prompt,chatHistory):
        classification_system_prompt = self.create_classification_prompt(self.endpoints)
        messageList=[
            {
              "role": "system",
              "content": classification_system_prompt ,
            },
            {
              "role": "user",
              "content": '\n"userCommand":"'+user_prompt+'","apiCallHistory":"'+str(chatHistory)+'"',
            }
          ]
        response = self.callLLM(messageList)
        
        #print(response)
        responseDict = eval(response)
        if isinstance(responseDict, list):
          responseDict = responseDict[0]
        endPoint = responseDict['apiCall']
        return endPoint

    def get_endpoint_info(self, endpoint_name):
        """ Get information about a registered endpoint """
        return self.endpoints.get(endpoint_name, None)

    def derive_params(self,endpoint,user_prompt,chatHistory):
      system_prompt = self.generalInstruction+'''\
As an AI assistant, your task is to analyze a user's command and chat history to derive the necessary parameters for a specific API endpoint. Use a short chain-of-thought approach to logically process the information provided and identify key parameters required for the API call based on the schema: \n\n

Consider the following steps in your reasoning:
1. Review the user's command and any relevant chat history.
2. Identify and list the parameters required by the endpoint's schema.
3. Match the elements from the user's input to the identified parameters.
4. If certain required parameters are missing or unclear, specify what additional information is needed. Keep the reasoning short.\n\nSchema:\n'''+self.endpoints[endpoint]['schema']+"\n\nSpecial Instruction :\n"+'''\
Your response should be a well-reasoned, step-by-step explanation of how each parameter is derived, culminating in a JSON-formatted output. If the user's input does not provide enough information for certain parameters, clearly state what is missing in a JSON-formatted error message. In case of error, do not generate any other parameters.

Expected Successful Output Format:
{"reasoning": "[Your step-by-step reasoning. Make sure no double quote is used within reasoning.]", "param1": "value1", "param2": "value2", ..., "paramN": "valueN"}

Expected Error Output Format:
{"error": "Please provide [missing parameter] so that we can proceed."}

Apply this methodical approach to ensure clarity and precision in deriving the necessary API call parameters. For every query, rely on the part of chatHistory which is relevant. Most of the chatHistory maynot be relevant for the query. Highlight this in reasoning. Following are some examples of user query and expected output.\n '''
      user_prompt = '\nThis is the latest query along with chatHistory for which parameters need to found out,\n {"Special_Instruction":"'+self.endpoints[endpoint]['splInstruction']+'","chatHistory":'+str(chatHistory)+',"userCommand":"'+user_prompt+'"}\n'+"Return back a single Json formatted output with reasoning and params. Do not generate any other comment/text appart from reasoning and parameter value pairs in one single JSON .Do not use double quotes inside reasoning. Use escaping with \\"
      messageList=[{"role": "system","content": system_prompt}]
      messageList.extend(self.endpoints[endpoint]['exampleList'])
      messageList.append({"role": "user","content": user_prompt})
      response = self.callLLM(messageList)
      response = response.replace('\\','')
      response = response.replace('false','False')
      response = response.replace('true','True')
      response = response.replace('null','None')
      #print(response)
      '''
      try:
        response = json.loads(response)
      except:
        response = self.extract_json_response(response)
      '''
      return eval(response)

    def processMessage(self,userPrompt):
        endpoint = self.classifyEndpoint(userPrompt,[])
        response = self.derive_params(endpoint,userPrompt,self.chatHistory)
        #print(response)
        if 'error' in response:
          return(response['error'])

        if 'reasoning' in response:
          del response['reasoning']

        #print(response)

        if endpoint == 'create_app':
          name = response['name']
          desc = response['desc']
          apiResponse = self.endpoints[endpoint]['function'](functionClient=self.functionClient,name=name,desc=desc)
          print (apiResponse)
        elif endpoint == 'set_view_tabs':
          app_id = response['app_id']
          path = response['path']
          apiResponse = self.endpoints[endpoint]['function'](functionClient=self.functionClient,app_id = app_id,path=path)
          print("View set to tabs successfully")
        elif endpoint == 'create_tabs':
          app_id =  response['app_id']
          path =  response['path']
          tab_id =  response['id']
          tabSeq =  response['tabSeq']
          tabTitle =  response['title']
          try:
             query =  response['feedConfig']['query']
          except:
              query = None
          apiResponse = self.endpoints[endpoint]['function'](functionClient=self.functionClient,app_id = app_id,path=path,tab_id=tab_id,tabSeq=tabSeq,tabTitle=tabTitle,query=query)
          print("Tab created successfully")
        
        elif endpoint == 'set_view_list':
          app_id = response['app_id']
          path = response['path']
          apiResponse = self.endpoints[endpoint]['function'](functionClient=self.functionClient,app_id = app_id,path=path)
          print("View set to list successfully")
        elif endpoint == 'create_posts_pie':
          app_id = response['app_id']
          folder_id = self.formatFolder(response['folder_id'])
          if 'id' in response:
            chartId = response['id']
          else:
            chartId = response['chartId']
          chartTitle = response['title']
          xData = response['x']
          yData = response['label']
          filters = response['filters']
          replaceKeyList = []
          for key, value in filters.items():
            if key.startswith('features.'):
              replaceKeyList.append(key)
          for key in replaceKeyList :
              newKey = key.replace('features.','')
              filters[newKey] = filters[key]
          for key in replaceKeyList :
            del filters[key]

          filters["dateAdded"] =  datetime.now().isoformat() + 'Z'

          apiResponse = self.endpoints[endpoint]['function'](functionClient=self.functionClient,app_id=app_id,folder_id=folder_id,chartId=chartId,chartTitle=chartTitle,xData=xData,yData=yData,filters=filters)
          print("Pie Chart created successfully")

        elif endpoint == 'create_posts_cartesian':
          app_id = response['app_id']
          folder_id = self.formatFolder(response['folder_id'])
          if 'id' in response:
            chartId = response['id']
          else:
            chartId = response['chartId']
          chartTitle = response['title']
          filters = response['filters']
          series = response['series']
          xAxisType = response['xAxisType']
          xAxisLabel = response['xAxisLabel']
          yAxisLabel = response['yAxisLabel']
          replaceKeyList = []
          for key, value in filters.items():
            if key.startswith('features.'):
              replaceKeyList.append(key)
          for key in replaceKeyList :
              newKey = key.replace('features.','')
              filters[newKey] = filters[key]
          for key in replaceKeyList :
            del filters[key]

          filters["dateAdded"] =  datetime.now().isoformat() + 'Z'

          apiResponse = self.endpoints[endpoint]['function'](functionClient=self.functionClient,app_id=app_id,folder_id=folder_id,chartId=chartId,chartTitle=chartTitle,series=series,xAxisType=xAxisType,xAxisLabel=xAxisLabel,yAxisLabel=yAxisLabel ,filters=filters)
          print("Cartesian chart created successfully")
        
        elif endpoint == 'set_view_table':
          if 'tableConfig' in response:
            data = response['tableConfig']
          else:
            data = response.copy()
            del data['app_id']
            del data['path']
          apiResponse = self.endpoints[endpoint]['function'](self.functionClient,response['app_id'],response['path'],data)
          print("View set to table successfully")
        elif endpoint == "create_posts_data":
          app_id = response['app_id']
          folder_id = self.formatFolder(response['folder_id'])
          id = response['id']
          data = response['data']
          filters = response['filters']

          replaceKeyList = []
          for key, value in filters.items():
            if key.startswith('features.'):
              replaceKeyList.append(key)
          for key in replaceKeyList :
              newKey = key.replace('features.','')
              filters[newKey] = filters[key]
          for key in replaceKeyList :
            del filters[key]

          filters["dateAdded"] =  datetime.now().isoformat() + 'Z'
          apiResponse = self.endpoints[endpoint]['function'](functionClient=self.functionClient,app_id=app_id,folder_id=folder_id,id=id,data=data,filters=filters)
          print("Post added successfully")

        self.chatHistory.append(json.dumps({'userCommand':userPrompt,'detectedEndpoint':endpoint,'generatedParams':response,'apiResponse':apiResponse}))
        #self.chatHistory.append(json.dumps({'userCommand':userPrompt,'apiResponse':apiResponse}))

