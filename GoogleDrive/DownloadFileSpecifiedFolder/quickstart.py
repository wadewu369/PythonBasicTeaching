from __future__ import print_function
import os
import io
import time
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload, MediaIoBaseDownload
from httplib2 import Http
from oauth2client import file, client, tools

# 權限必須
SCOPES = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

getDownloadFileIdList = []
getDownloadFileNameList = []

def delete_drive_service_file(service, file_id):
    service.files().delete(fileId=file_id).execute()


def search_folder(service, drive_service_folder_name=None):
    """
    如果雲端資料夾名稱相同，則只會選擇一個資料夾上傳，請勿取名相同名稱
    :param service: 認證用
    :param update_drive_folder_name: 取得指定資料夾的id，沒有的話回傳None，給錯也會回傳None
    :return:
    """
    get_folder_id_list = []
    if drive_service_folder_name is not None:
        response = service.files().list(fields="nextPageToken, files(id, name)", spaces='drive',
                                       q = "name = '" + drive_service_folder_name + "' and mimeType = 'application/vnd.google-apps.folder' and trashed = false").execute()
        for file in response.get('files', []):
            print('雲端資料夾: %s (%s)' % (file.get('name'), file.get('id')))
            return file.get('id')
        if len(get_folder_id_list) == 0:
            print("找不到你所提供的資料夾名稱，因此會搜尋整個雲端檔案\n 如果有發現符合檔案名稱，則會自動下載至本地端")
            return None
        else:
            return file.get('id')
    return None


def download_file(service, file_id_list, file_name_list, download_file_path, ):
    """
    雲端將資料下載到本地端用

    :param service: 認證用
    :param file_id_list: 雲端檔案的id 可透過 update_file()取得
    :param download_file_path: 將雲端上的資料下載到本地端的位置
    :param download_file_name: 下載到本地端的名稱
    :return:
    """
    print(file_id_list)
    print(file_name_list)
    if file_id_list is not None:
        for times in range(len(file_id_list)):
            request = service.files().get_media(fileId=file_id_list[times])
            local_download_path = download_file_path + file_name_list[times]
            fh = io.FileIO(local_download_path, 'wb')
            downloader = MediaIoBaseDownload(fh, request)
            print("下載檔案中....")
            done = False
            while done is False:
                status, done = downloader.next_chunk()
                print("Download %d%%." % int(status.progress() * 100))
            print("下載完成")
            print("下載檔案位置為: ", str(local_download_path))
            print("=====下載檔案完成=====")
    else:
        print("=====下載檔案失敗，未找到檔案=====")


def search_file(service, download_drive_service_name, folder_id, is_delete_search_file=False):
    # global getDownloadFileIdList
    # global getDownloadFileNameList
    """
    本地端
    取得到雲端名稱，可透過下載時，取得file id 下載

    :param service: 認證用
    :param download_drive_service_name: 要上傳到雲端的名稱
    :param is_delete_search_file: 判斷是否需要刪除這個檔案名稱
    :return:
    """

    # Call the Drive v3 API
    # if download_drive_service_name is None:
    #     return None
    # else:
    results = service.files().list(fields="nextPageToken, files(parents, id, name)", spaces='drive',
                                   q="trashed = false",
                                   ).execute()
    items = results.get('files', [])
    for item in items:
        try:
            getItemStr = ''.join(item['parents'])
            if getItemStr == folder_id:
                getDownloadFileIdList.append(item['id'])
                getDownloadFileNameList.append(item['name'])
        except Exception as e:
            pass
    print('取得資料夾內的檔案id: %s' % ', '.join(getDownloadFileIdList))
    print('取得資料夾內的檔案id: %s' % ', '.join(getDownloadFileNameList))

    # return getDownloadFileIdList


def main(is_download_file_function=False, download_drive_service_name=None, download_file_path=None, drive_service_folder_name=None):
    """
    :param is_download_file_function: 判斷是否執行下載的功能
    :param download_drive_service_name: 要上傳到雲端上的檔案名稱
    :param download_file_path: 要下載的位置以及名稱
    :return:
    """

    print("is_download_file_function: %s " % is_download_file_function)
    print("drive_service_folder_name: %s " % drive_service_folder_name)
    store = file.Storage('token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('drive', 'v3', http=creds.authorize(Http()))
    print('*' * 10)

    # 本地端 執行部分
    if is_download_file_function is True:
        print("=====執行下載檔案=====")
        # 搜尋上傳的檔案名稱 本地端執行部分
        get_folder_id = search_folder(service = service, drive_service_folder_name = drive_service_folder_name)
        search_file(service=service, download_drive_service_name=download_drive_service_name, folder_id = get_folder_id)
        download_file(service=service, file_id_list =getDownloadFileIdList, download_file_path=download_file_path,
                      file_name_list=getDownloadFileNameList)


if __name__ == '__main__':
    main(is_download_file_function=bool(True), drive_service_folder_name='TestAPI', download_drive_service_name=None, download_file_path=os.getcwd() + '/')



