import os
import requests
import chardet
import logging
import xml.etree.ElementTree as ET

from pathlib import Path
from time import sleep


FORMAT = '%(message)s'
logging.basicConfig(format=FORMAT, level=logging.INFO)
log = logging.getLogger(__name__)


# class to download or upload data from/to .Stat Suite
class Download_upload():

    # Declare constants
    __ERROR  = "An error occurred: "
    __NO_ACCESS_TOKEN = "No access token"
    __EXECUTION_IN_QUEUED = "Queued"
    __EXECUTION_IN_PROGRESS = "InProgress"
    __DOWNLOAD_SUCCESS = "Successful download"
    __UPLOAD_SUCCESS = "The request was successfully processed "
    __UPLOAD_FAILED = "The request failed with status code "

    __NAMESPACE_MESSAGE = "{http://www.sdmx.org/resources/sdmxml/schemas/v2_1/message}"
    __NAMESPACE_COMMON = "{http://www.sdmx.org/resources/sdmxml/schemas/v2_1/common}"
  
    # Initialise Download_upload
    def __init__(self, adfsAuthentication_obj, access_token):
        self.adfsAuthentication_obj = adfsAuthentication_obj
        self.access_token = access_token

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.adfsAuthentication_obj = None
        self.access_token = None


    # Download a file from .STAT
    def download_file(self, dotstat_url: str, content_format: str, file_path: Path):
        try:
            Returned_Message = ""

            if (self.access_token == None):
                Returned_Message = self.__ERROR  + self.__NO_ACCESS_TOKEN + os.linesep

                # Write the result to the log
                for line in Returned_Message.split(os.linesep):
                    if len(line) > 0:
                        log.info('   ' + line)
            else:
                if self.adfsAuthentication_obj.is_access_token_expired():
                    self.access_token = self.adfsAuthentication_obj.get_token()

                headers = {
                   'accept': content_format,
                   'authorization': 'Bearer '+self.access_token
                }

                #
                response = requests.get(dotstat_url, verify=True, headers=headers)
        except Exception as err:
            Returned_Message = self.__ERROR  + str(err) + os.linesep

            # Write the result to the log
            for line in Returned_Message.split(os.linesep):
                if len(line) > 0:
                    log.info('   ' + line)
        else:
            if response.status_code != 200:
                Returned_Message = self.__ERROR  + 'Error code: ' + \
                    str(response.status_code) + ' Reason: ' + str(response.reason)
                if len(response.text) > 0:
                    Returned_Message += os.linesep + 'Text: ' + response.text
            else:
                if os.path.isfile(file_path):
                    os.remove(file_path)
                with open(file_path, "wb") as file:
                    file.write(response.content)
                    Returned_Message = self.__DOWNLOAD_SUCCESS
            
            # Write the result to the log
            for line in Returned_Message.split(os.linesep):
                if len(line) > 0:
                    log.info('   ' + line)
        finally:
            return Returned_Message


    # Download streamed content from .STAT
    def download_stream(self, dotstat_url: str, content_format: str):
        try:
            Returned_Message = ""

            if (self.access_token == None):
                Returned_Message = self.__ERROR  + self.__NO_ACCESS_TOKEN + os.linesep
            else:
                if self.adfsAuthentication_obj.is_access_token_expired():
                    self.access_token = self.adfsAuthentication_obj.get_token()

                headers = {
                    'accept': content_format,
                    'Transfer-Encoding': 'chunked',
                    'authorization': 'Bearer '+self.access_token
                }

                #
                return requests.get(dotstat_url, verify=True, headers=headers, stream=True)
        except Exception as err:
            Returned_Message = self.__ERROR  + str(err) + os.linesep
            return Returned_Message


    # Upload a file to .STAT
    def upload_file(self, 
                    transfer_url: str, 
                    file_path: Path, 
                    space: str, 
                    validationType: int, 
                    use_filepath: bool = False):
        try:
            Returned_Message = ""

            if (self.access_token == None):
                Returned_Message = self.__ERROR  + self.__NO_ACCESS_TOKEN + os.linesep

                # Write the result to the log
                for line in Returned_Message.split(os.linesep):
                    if len(line) > 0:
                        log.info('   ' + line)
            else:
                if self.adfsAuthentication_obj.is_access_token_expired():
                    self.access_token = self.adfsAuthentication_obj.get_token()

                payload = {
                    'dataspace': space,
                    'validationType': validationType
                }

                headers = {
                    'accept': 'application/json',
                    'authorization': "Bearer "+self.access_token
                }

                if  use_filepath:
                    files = {
                        'dataspace': (None, payload['dataspace']),
                        'validationType': (None, payload['validationType']),
                        'filepath': (None, os.path.realpath(file_path))
                    }
                else:
                    files = {
                        'dataspace': (None, payload['dataspace']),
                        'validationType': (None, payload['validationType']),
                        'file': (os.path.realpath(file_path), open(os.path.realpath(file_path), 'rb'), 'text/csv', '')
                    }

                #
                response = requests.post(transfer_url, verify=True, headers=headers, files=files)
        except Exception as err:
            Returned_Message = self.__ERROR  + str(err) + os.linesep

            # Write the result to the log
            for line in Returned_Message.split(os.linesep):
                if len(line) > 0:
                    log.info('   ' + line)
        else:
            if response.status_code != 200:
                Returned_Message = self.__ERROR  + 'Error code: ' + \
                    str(response.status_code) + ' Reason: ' + str(response.reason)
                if len(response.text) > 0:
                    Returned_Message = Returned_Message + os.linesep + 'Text: ' + response.text

                Returned_Message = Returned_Message + os.linesep
                # Write the result to the log
                for line in Returned_Message.split(os.linesep):
                    if len(line) > 0:
                        log.info('   ' + line)
            else:
                try:
                    Result = response.json()['message']

                    # Write the result to the log
                    for line in Result.split(os.linesep):
                        if len(line) > 0:
                            log.info('   ' + line)

                    Returned_Message = Result + os.linesep

                    # Check the request status
                    if (Result != "" and Result.find(self.__ERROR ) == -1):
                        # Extract the request ID the returned message
                        start = 'with ID'
                        end = 'was successfully'
                        requestId = Result[Result.find(
                            start)+len(start):Result.rfind(end)]

                        # Sleep a little bit before checking the request status
                        sleep(3)

                        # To avoid this error: maximum recursion depth exceeded while calling a Python object
                        # replace the recursive calls with while loops.
                        Result = self.__check_request_status(transfer_url, requestId, space)

                        # Write the result to the log
                        for line in Result.split(os.linesep):
                            if len(line) > 0:
                                log.info('   ' + line)
                        sleep(3)

                        Previous_Result = Result
                        while Result in [self.__EXECUTION_IN_PROGRESS, self.__EXECUTION_IN_QUEUED]:
                            Result = self.__check_request_status(transfer_url, requestId, space)

                            # Prevent loging again the same information such as "Queued" or "InProgress" 
                            if Previous_Result != Result:
                               Previous_Result = Result

                            # Write the result to the log
                            for line in Previous_Result.split(os.linesep):
                              if (len(line) > 0 and line not in [self.__EXECUTION_IN_PROGRESS, self.__EXECUTION_IN_QUEUED]):
                                 log.info('   ' + line)
                            sleep(3)

                        Returned_Message = Returned_Message + Result + os.linesep
                except Exception as err:
                    Returned_Message = self.__ERROR  + str(err) + os.linesep
                    if len(response.text) > 0:
                        Returned_Message = Returned_Message + 'Text: ' + response.text + os.linesep

                    # Write the result to the log
                    for line in Returned_Message.split(os.linesep):
                        if len(line) > 0:
                            log.info('   ' + line)
        finally:
            return Returned_Message


    # Upload a structure to .STAT
    def upload_structure(self, transfer_url: str, file_path: Path):
        try:
            Returned_Message = ""

            if (self.access_token == None):
                Returned_Message = self.__ERROR  + self.__NO_ACCESS_TOKEN + os.linesep

                # Write the result to the log
                for line in Returned_Message.split(os.linesep):
                    if len(line) > 0:
                        log.info('   ' + line)
            else:
                if self.adfsAuthentication_obj.is_access_token_expired():
                    self.access_token = self.adfsAuthentication_obj.get_token()

                # Detect the encoding used in file 
                detected_encoding = self.__detect_encode(file_path)

                # Read file as a string "r+" with the detected encoding
                with open(file=file_path, mode="r+", encoding=detected_encoding.get("encoding")) as file:
                    xml_data = file.read()

                # Make sure the encoding is "utf-8"
                tree = ET.fromstring(xml_data)
                xml_data = ET.tostring(tree, encoding="utf-8", method='xml', xml_declaration=True)

                headers = {
                    'Content-Type': 'application/xml',
                    'authorization': "Bearer "+self.access_token
                }

                #
                response = requests.post(transfer_url, verify=True, headers=headers, data=xml_data)
        except Exception as err:
            Returned_Message = self.__ERROR  + str(err) + os.linesep

            # Write the result to the log
            for line in Returned_Message.split(os.linesep):
                if len(line) > 0:
                    log.info('   ' + line)
        else:
            try:
                response.raise_for_status()
            except requests.exceptions.HTTPError as e:
                Returned_Message = f'{self.__UPLOAD_FAILED}{response.status_code}: {e}'

                # Write the result to the log
                for line in Returned_Message.split(os.linesep):
                    if len(line) > 0:
                        log.info('   ' + line)
            else:
                response_tree = ET.XML(response.content)
                for error_message in response_tree.findall("./{0}ErrorMessage".format(self.__NAMESPACE_MESSAGE)):
                    text_element = error_message.find("./{0}Text".format(self.__NAMESPACE_COMMON))
                    if (text_element is not None):
                        if Returned_Message == "":
                            Returned_Message = self.__UPLOAD_SUCCESS + os.linesep
                        Returned_Message = Returned_Message + text_element.text + os.linesep

                # Write the result to the log
                for line in Returned_Message.split(os.linesep):
                    if len(line) > 0:
                        log.info('   ' + line)
        finally:
            return Returned_Message
        

    # Detect the encoding used in file
    def __detect_encode(self, file_path):
        detector = chardet.UniversalDetector()
        detector.reset()
        with open(file=file_path, mode="rb") as file:
            for row in file:
                detector.feed(row)
                if detector.done: 
                    break

        detector.close()

        return detector.result


    # Check request sent to .STAT status
    # To avoid this error: maximum recursion depth exceeded while calling a Python object
    # replace the recursive calls with while loops.
    def __check_request_status(self, transfer_url, requestId, space):
        try:
            Returned_Message = ""

            if (self.access_token == None):
                Returned_Message = self.__ERROR  + self.__NO_ACCESS_TOKEN + os.linesep
            else:
                if self.adfsAuthentication_obj.is_access_token_expired():
                    self.access_token = self.adfsAuthentication_obj.get_token()

                headers = {
                    'accept': 'application/json',
                    'authorization': "Bearer "+self.access_token
                }

                payload = {
                    'dataspace': space,
                    'id': requestId
                }

                transfer_url = transfer_url.replace("import", "status")
                transfer_url = transfer_url.replace("sdmxFile", "request")

                #
                response = requests.post(transfer_url, verify=True, headers=headers, data=payload)
        except Exception as err:
            Returned_Message = self.__ERROR  + str(err)
        else:
            if response.status_code != 200:
                Returned_Message = self.__ERROR  + 'Error code: ' + \
                    str(response.status_code) + ' Reason: ' + str(response.reason)
                if len(response.text) > 0:
                    Returned_Message = Returned_Message + os.linesep + 'Text: ' + response.text
            else:
                executionStatus = 'Execution status: ' + response.json()['executionStatus']
                if response.json()['executionStatus'] in [self.__EXECUTION_IN_PROGRESS, self.__EXECUTION_IN_QUEUED]:
                    Returned_Message = response.json()['executionStatus']
                else:
                    Returned_Message = executionStatus + os.linesep + 'Outcome: ' + response.json()['outcome'] + os.linesep
                    index = 0
                    while index < len(response.json()['logs']):
                        Returned_Message = Returned_Message + 'Log' + str(index) + ': ' + response.json()['logs'][index]['message'] + os.linesep
                        index += 1
        finally:
            return Returned_Message
    