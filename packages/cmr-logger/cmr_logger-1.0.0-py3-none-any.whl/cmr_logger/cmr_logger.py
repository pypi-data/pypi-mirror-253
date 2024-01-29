import logging
from typing import Union
import functools
import JSONLogger
import time
import inspect
from pathlib import Path
import sys
import pickle
import json
import sys
import traceback
from datetime import datetime
import os
from json import JSONEncoder

class CMRLoggerEncoder(JSONEncoder):
        def default(self, o):
            return o.__dict__    
        
class CMRLoggingOtherInfo:
    fileId = 0
    fieldId = 0
    userId = 0
    batchId = 0
    fieldName = ""
    exactFileName =""
    clientId = 0

class CMRLoggerHandler:
    def __init__(self):
        logging.basicConfig(level=logging.DEBUG)

    def get_logger(self, moduleName=None):
        return logging.getLogger(moduleName)
    
    def setCustomAttributes(self, cmrLoggingOtherInfo,moduleName =None):
        cmrlogger = logging.getLogger(moduleName)
        cmrlogger.cmrLoggingOtherInfo = cmrLoggingOtherInfo

    def LogDebugMessage(self,moduleName,debugMessage,cmrLoggingOtherInfoParam = None):

        def get_class_from_frame(fr):
            args, _, _, value_dict = inspect.getargvalues(fr)
            # we check the first parameter for the frame function is
            # named 'self'
            if len(args) and args[0] == 'self':
                # in that case, 'self' will be referenced in value_dict
                instance = value_dict.get('self', None)
                if instance:
                    # return its class
                    return getattr(instance, '__class__', None)
            # return None otherwise
            return None

        cmrlogger = logging.getLogger(moduleName)
        if(cmrLoggingOtherInfoParam is None):
            cmrlogger.cmrLoggingOtherInfo = CMRLoggingOtherInfo()
        else:
            cmrlogger.cmrLoggingOtherInfo = cmrLoggingOtherInfoParam    

        old_factoryResultExp = logging.getLogRecordFactory()
        functionCallFromSubModule =""
        functionCallFromMethod =""
        parameterList =""
        resultDump =""
        exceptionType =""
               
        skip=1
        stack = inspect.stack()
        start = 0 + skip
        functionCallFromSubModule =""

        if len(stack) < start + 1:
            details = ''
        parentframe = stack[start][0]
        classname = get_class_from_frame(parentframe)

        if(classname is not None):
            functionCallFromSubModule = stack[1][0].f_locals["self"].__class__.__name__
            functionCallFromMethod = stack[1][0].f_code.co_name
                 
            # pull tuple from frame
            args, args_paramname, kwargs_paramname, values = inspect.getargvalues(
                parentframe)
        
            # show formal parameters
            for i in (args if args is not None else []):
                parameterList = parameterList +"\t{}={}".format(i, values[i])
       

            # show positional varargs
            if args_paramname is not None:
                varglist = values[args_paramname]
                for v in (varglist if varglist is not None else []):
                    parameterList = parameterList + "\t*{}={}".format(args_paramname, v)

            # show named varargs
            if kwargs_paramname is not None:
                varglist = values[kwargs_paramname]
                for k in (sorted(varglist) if varglist is not None else []):
                    parameterList = parameterList + "\t*{} {}={}".format(kwargs_paramname, k, varglist[k])

        else:
            if __name__ in stack[1][0].f_locals:
              functionCallFromSubModule = stack[1][0].f_locals["__name__"] 
            else:
                functionCallFromMethod = stack[1][3]
                methodcall = stack[3][4][0].split('.')
                if len(methodcall) > 0:
                    if len(methodcall) == 1:
                        functionCallFromSubModule = ""
                        parameterList = methodcall[0]
                    else:
                        functionCallFromSubModule = methodcall[0]
                        parameterList = methodcall[1]


        # call line.
        line = parentframe.f_lineno

        # Remove reference to frame
        del parentframe

        def setCustomeAttributesInLogRecord(record):
            record.CMRBatchId = cmrlogger.cmrLoggingOtherInfo.batchId
            record.CMRFileId = cmrlogger.cmrLoggingOtherInfo.fileId
            record.CMRProcessedFileName = cmrlogger.cmrLoggingOtherInfo.exactFileName
            record.CMRFieldId = cmrlogger.cmrLoggingOtherInfo.fieldId
            record.CMRFieldName = cmrlogger.cmrLoggingOtherInfo.fieldName
            record.CMRUserID = cmrlogger.cmrLoggingOtherInfo.userId
            record.CMRClientId = cmrlogger.cmrLoggingOtherInfo.clientId

        def record_factoryResultException(*args, **kwargs):
            record = old_factoryResultExp(*args, **kwargs)
            record.CMRTimeStamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S,%f')[:-3]
            record.CMRSubModule = functionCallFromSubModule
            record.CMRMethod = functionCallFromMethod
            record.CMRMethodInput = parameterList
            record.CMRMethodOutput = resultDump
            record.CMRExceptionType = exceptionType
            record.CMRMethodExecutionDuration = 0
            record.CMRErrorMessage = ""
            record.CMRStackTrace = ""
            setCustomeAttributesInLogRecord(record)
            return record
        
        logging.setLogRecordFactory(record_factoryResultException)  
        
        errHandler, stdoutHandler = GetLoggingHandlers(moduleName)

        # Add each handler to the Logger object
        # 'adding handlers- '
        # allows to add only one instance of file handler and stream handler
        AddLoggingHandlers(cmrlogger, errHandler, stdoutHandler)
            # 'added handlers for the first time'
        fmt = SetDebugJsonFormatter()
        stdoutHandler.setFormatter(fmt)
        errHandler.setFormatter(fmt)
              
        cmrlogger.debug(debugMessage)

    def LogExceptionMessage(self,moduleName,expMessage,exceptionType="", cmrLoggingOtherInfoParam = None):
           # print("type of cmrLoggingOtherInfoParam" + str(type(cmrLoggingOtherInfoParam)))
            def get_class_from_frame(fr):
                args, _, _, value_dict = inspect.getargvalues(fr)
                # we check the first parameter for the frame function is
                # named 'self'
                if len(args) and args[0] == 'self':
                    # in that case, 'self' will be referenced in value_dict
                    instance = value_dict.get('self', None)
                    if instance:
                        # return its class
                        return getattr(instance, '__class__', None)
                # return None otherwise
                return None

            cmrlogger = logging.getLogger(moduleName)
            if(cmrLoggingOtherInfoParam is None):
                cmrlogger.cmrLoggingOtherInfo = CMRLoggingOtherInfo()
            else:
                cmrlogger.cmrLoggingOtherInfo = cmrLoggingOtherInfoParam  

            old_factoryResultExp = logging.getLogRecordFactory()
            functionCallFromSubModule =""
            functionCallFromMethod =""
            parameterList =""
            resultDump =""
          
                
            skip=1
            stack = inspect.stack()
            start = 0 + skip
            functionCallFromSubModule =""

            if len(stack) < start + 1:
                details = ''
            parentframe = stack[start][0]
            classname = get_class_from_frame(parentframe)
            parameterList = ""
            functionCallFromMethod = ""
            if(classname is not None):
                functionCallFromSubModule = stack[1][0].f_locals["self"].__class__.__name__
                functionCallFromMethod = stack[1][0].f_code.co_name
            
            
                # pull tuple from frame
                args, args_paramname, kwargs_paramname, values = inspect.getargvalues(
                    parentframe)

            
                # show formal parameters
                for i in (args if args is not None else []):
                    parameterList = parameterList +"\t{}={}".format(i, values[i])
            

                # show positional varargs
                if args_paramname is not None:
                    varglist = values[args_paramname]
                    for v in (varglist if varglist is not None else []):
                        parameterList = parameterList + "\t*{}={}".format(args_paramname, v)

                # show named varargs
                if kwargs_paramname is not None:
                    varglist = values[kwargs_paramname]
                    for k in (sorted(varglist) if varglist is not None else []):
                        parameterList = parameterList + "\t*{} {}={}".format(kwargs_paramname, k, varglist[k])

            else:
                if __name__ in stack[1][0].f_locals:
                   functionCallFromSubModule = stack[1][0].f_locals["__name__"] 
                else:
                    functionCallFromMethod = stack[1][3]
                    methodcall = stack[3][4][0].split('.')
                    if len(methodcall) > 0:
                        if len(methodcall) == 1:
                            functionCallFromSubModule = ""
                            parameterList = methodcall[0]
                        else:
                            functionCallFromSubModule = methodcall[0]
                            parameterList = methodcall[1]
    
            # call line.
            line = parentframe.f_lineno

            # Remove reference to frame
            del parentframe

            def record_factoryResultException(*args, **kwargs):
                record = old_factoryResultExp(*args, **kwargs)
                record.CMRTimeStamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S,%f')[:-3]
                record.CMRSubModule = functionCallFromSubModule
                record.CMRMethod = functionCallFromMethod
                record.CMRMethodInput = parameterList
                record.CMRMethodOutput = resultDump
                record.CMRExceptionType = exceptionType
                record.CMRMethodExecutionDuration = 0
                record.CMRErrorMessage = expMessage
                record.CMRStackTrace = ""

                setCustomeAttributesInLogRecord(record)
                return record
            
            def setCustomeAttributesInLogRecord(record):
                record.CMRBatchId = cmrlogger.cmrLoggingOtherInfo.batchId
                record.CMRFileId = cmrlogger.cmrLoggingOtherInfo.fileId
                record.CMRProcessedFileName = cmrlogger.cmrLoggingOtherInfo.exactFileName
                record.CMRFieldId = cmrlogger.cmrLoggingOtherInfo.fieldId
                record.CMRFieldName = cmrlogger.cmrLoggingOtherInfo.fieldName
                record.CMRUserID = cmrlogger.cmrLoggingOtherInfo.userId
                record.CMRClientId = cmrlogger.cmrLoggingOtherInfo.clientId

            logging.setLogRecordFactory(record_factoryResultException)  

            # Add each handler to the Logger object
            # 'adding handlers- '
            # allows to add only one instance of file handler and stream handler
            errHandler, stdoutHandler = GetLoggingHandlers(moduleName)
            AddLoggingHandlers(cmrlogger, errHandler, stdoutHandler)
            # 'added handlers for the first time'
            fmt = SetErrorJSONFormatter()
            stdoutHandler.setFormatter(fmt)
            errHandler.setFormatter(fmt)
    
            cmrlogger.error(expMessage) #, args,exc_info,stack_info,stacklevel)    

    def LogCriticalMessage(self,moduleName,expMessage,exceptionType="", cmrLoggingOtherInfoParam = None):
            def get_class_from_frame(fr):
                args, _, _, value_dict = inspect.getargvalues(fr)
                # we check the first parameter for the frame function is
                # named 'self'
                if len(args) and args[0] == 'self':
                    # in that case, 'self' will be referenced in value_dict
                    instance = value_dict.get('self', None)
                    if instance:
                        # return its class
                        return getattr(instance, '__class__', None)
                # return None otherwise
                return None

            cmrlogger = logging.getLogger(moduleName)
            if(cmrLoggingOtherInfoParam is None):
                cmrlogger.cmrLoggingOtherInfo = CMRLoggingOtherInfo()
            else:
                cmrlogger.cmrLoggingOtherInfo = cmrLoggingOtherInfoParam  

            old_factoryResultExp = logging.getLogRecordFactory()
            functionCallFromSubModule =""
            functionCallFromMethod =""
            parameterList =""
            resultDump =""
          
                
            skip=1
            stack = inspect.stack()
            start = 0 + skip
            functionCallFromSubModule =""

            if len(stack) < start + 1:
                details = ''
            parentframe = stack[start][0]
            classname = get_class_from_frame(parentframe)
            parameterList = ""
            functionCallFromMethod = ""
            if(classname is not None):
                functionCallFromSubModule = stack[1][0].f_locals["self"].__class__.__name__
                functionCallFromMethod = stack[1][0].f_code.co_name
            
            
                # pull tuple from frame
                args, args_paramname, kwargs_paramname, values = inspect.getargvalues(
                    parentframe)

            
                # show formal parameters
                for i in (args if args is not None else []):
                    parameterList = parameterList +"\t{}={}".format(i, values[i])
            

                # show positional varargs
                if args_paramname is not None:
                    varglist = values[args_paramname]
                    for v in (varglist if varglist is not None else []):
                        parameterList = parameterList + "\t*{}={}".format(args_paramname, v)

                # show named varargs
                if kwargs_paramname is not None:
                    varglist = values[kwargs_paramname]
                    for k in (sorted(varglist) if varglist is not None else []):
                        parameterList = parameterList + "\t*{} {}={}".format(kwargs_paramname, k, varglist[k])

            else:
                if __name__ in stack[1][0].f_locals:
                   functionCallFromSubModule = stack[1][0].f_locals["__name__"] 
                else:
                    functionCallFromMethod = stack[1][3]
                    methodcall = stack[3][4][0].split('.')
                    if len(methodcall) > 0:
                        if len(methodcall) == 1:
                            functionCallFromSubModule = ""
                            parameterList = methodcall[0]
                        else:
                            functionCallFromSubModule = methodcall[0]
                            parameterList = methodcall[1]

            # call line.
            line = parentframe.f_lineno

            # Remove reference to frame
            del parentframe

            def record_factoryResultException(*args, **kwargs):
                record = old_factoryResultExp(*args, **kwargs)
                record.CMRTimeStamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S,%f')[:-3]
                record.CMRSubModule = functionCallFromSubModule
                record.CMRMethod = functionCallFromMethod
                record.CMRMethodInput = parameterList
                record.CMRMethodOutput = resultDump
                record.CMRExceptionType = exceptionType
                record.CMRMethodExecutionDuration = 0
                record.CMRErrorMessage = expMessage
                record.CMRStackTrace = ""

                setCustomeAttributesInLogRecord(record)
                return record
            
            def setCustomeAttributesInLogRecord(record):
                record.CMRBatchId = cmrlogger.cmrLoggingOtherInfo.batchId
                record.CMRFileId = cmrlogger.cmrLoggingOtherInfo.fileId
                record.CMRProcessedFileName = cmrlogger.cmrLoggingOtherInfo.exactFileName
                record.CMRFieldId = cmrlogger.cmrLoggingOtherInfo.fieldId
                record.CMRFieldName = cmrlogger.cmrLoggingOtherInfo.fieldName
                record.CMRUserID = cmrlogger.cmrLoggingOtherInfo.userId
                record.CMRClientId = cmrlogger.cmrLoggingOtherInfo.clientId

            logging.setLogRecordFactory(record_factoryResultException)  

            # Add each handler to the Logger object
            # 'adding handlers- '
            # allows to add only one instance of file handler and stream handler
            errHandler, stdoutHandler = GetLoggingHandlers(moduleName)
            AddLoggingHandlers(cmrlogger, errHandler, stdoutHandler)
            # 'added handlers for the first time'
            fmt = SetErrorJSONFormatter()
            stdoutHandler.setFormatter(fmt)
            errHandler.setFormatter(fmt)
    
            cmrlogger.critical(expMessage) #, args,exc_info,stack_info,stacklevel)    

    def LogWarningMessage(self,moduleName,warnMessage,cmrLoggingOtherInfoParam = None):
            def get_class_from_frame(fr):
                args, _, _, value_dict = inspect.getargvalues(fr)
                # we check the first parameter for the frame function is
                # named 'self'
                if len(args) and args[0] == 'self':
                    # in that case, 'self' will be referenced in value_dict
                    instance = value_dict.get('self', None)
                    if instance:
                        # return its class
                        return getattr(instance, '__class__', None)
                # return None otherwise
                return None

            cmrlogger = logging.getLogger(moduleName)
            if(cmrLoggingOtherInfoParam is None):
                cmrlogger.cmrLoggingOtherInfo = CMRLoggingOtherInfo()
            else:
                cmrlogger.cmrLoggingOtherInfo = cmrLoggingOtherInfoParam  

            old_factoryResultExp = logging.getLogRecordFactory()
            functionCallFromSubModule =""
            functionCallFromMethod =""
            parameterList =""
            resultDump =""
            exceptionType =""
                
            skip=1
            stack = inspect.stack()
            start = 0 + skip
            functionCallFromSubModule =""

            if len(stack) < start + 1:
                details = ''
            parentframe = stack[start][0]
            classname = get_class_from_frame(parentframe)
            parameterList = ""
            functionCallFromMethod = ""
            if(classname is not None):
                functionCallFromSubModule = stack[1][0].f_locals["self"].__class__.__name__
                functionCallFromMethod = stack[1][0].f_code.co_name
            
            
                # pull tuple from frame
                args, args_paramname, kwargs_paramname, values = inspect.getargvalues(
                    parentframe)

            
                # show formal parameters
                for i in (args if args is not None else []):
                    parameterList = parameterList +"\t{}={}".format(i, values[i])
            

                # show positional varargs
                if args_paramname is not None:
                    varglist = values[args_paramname]
                    for v in (varglist if varglist is not None else []):
                        parameterList = parameterList + "\t*{}={}".format(args_paramname, v)


                # show named varargs
                if kwargs_paramname is not None:
                    varglist = values[kwargs_paramname]
                    for k in (sorted(varglist) if varglist is not None else []):
                        parameterList = parameterList + "\t*{} {}={}".format(kwargs_paramname, k, varglist[k])

            else:
                if __name__ in stack[1][0].f_locals:
                   functionCallFromSubModule = stack[1][0].f_locals["__name__"] 
                else:
                    functionCallFromMethod = stack[1][3]
                    methodcall = stack[3][4][0].split('.')
                    if len(methodcall) > 0:
                        if len(methodcall) == 1:
                            functionCallFromSubModule = ""
                            parameterList = methodcall[0]
                        else:
                            functionCallFromSubModule = methodcall[0]
                            parameterList = methodcall[1]


            # call line.
            line = parentframe.f_lineno

            # Remove reference to frame
            del parentframe

            def record_factoryResultException(*args, **kwargs):
                record = old_factoryResultExp(*args, **kwargs)
                record.CMRTimeStamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S,%f')[:-3]
                record.CMRSubModule = functionCallFromSubModule
                record.CMRMethod = functionCallFromMethod
                record.CMRMethodInput = parameterList
                record.CMRMethodOutput = resultDump
                record.CMRExceptionType = exceptionType
                record.CMRMethodExecutionDuration = 0
                record.CMRErrorMessage = ""
                record.CMRStackTrace = ""

                setCustomeAttributesInLogRecord(record)
                return record
            
            def setCustomeAttributesInLogRecord(record):
                record.CMRBatchId = cmrlogger.cmrLoggingOtherInfo.batchId
                record.CMRFileId = cmrlogger.cmrLoggingOtherInfo.fileId
                record.CMRProcessedFileName = cmrlogger.cmrLoggingOtherInfo.exactFileName
                record.CMRFieldId = cmrlogger.cmrLoggingOtherInfo.fieldId
                record.CMRFieldName = cmrlogger.cmrLoggingOtherInfo.fieldName
                record.CMRUserID = cmrlogger.cmrLoggingOtherInfo.userId
                record.CMRClientId = cmrlogger.cmrLoggingOtherInfo.clientId

            logging.setLogRecordFactory(record_factoryResultException)  

            #Add each handler to the Logger object
            # 'adding handlers- '
            # allows to add only one instance of file handler and stream handler
            errHandler, stdoutHandler = GetLoggingHandlers(moduleName)
            AddLoggingHandlers(cmrlogger, errHandler, stdoutHandler)
            # 'added handlers for the first time'
            fmt = SetWarnJsonFormatter()
            stdoutHandler.setFormatter(fmt)
            errHandler.setFormatter(fmt)

            cmrlogger.warning(warnMessage)   

    def LogInfoMessage(self,moduleName,infoMessage,cmrLoggingOtherInfoParam = None):

        def get_class_from_frame(fr):
            args, _, _, value_dict = inspect.getargvalues(fr)
            # we check the first parameter for the frame function is
            # named 'self'
            if len(args) and args[0] == 'self':
                # in that case, 'self' will be referenced in value_dict
                instance = value_dict.get('self', None)
                if instance:
                    # return its class
                    return getattr(instance, '__class__', None)
            # return None otherwise
            return None

        cmrlogger = logging.getLogger(moduleName)
        if(cmrLoggingOtherInfoParam is None):
            cmrlogger.cmrLoggingOtherInfo = CMRLoggingOtherInfo()
        else:
            cmrlogger.cmrLoggingOtherInfo = cmrLoggingOtherInfoParam  

        old_factoryResultExp = logging.getLogRecordFactory()
        functionCallFromSubModule =""
        functionCallFromMethod =""
        parameterList =""
        resultDump =""
        exceptionType =""
               
        skip=1
        stack = inspect.stack()
        start = 0 + skip
        functionCallFromSubModule =""

        if len(stack) < start + 1:
            details = ''
        parentframe = stack[start][0]
        classname = get_class_from_frame(parentframe)
        parameterList = ""
        functionCallFromMethod = ""
        if(classname is not None):
            functionCallFromSubModule = stack[1][0].f_locals["self"].__class__.__name__
            functionCallFromMethod = stack[1][0].f_code.co_name
         
        
            # pull tuple from frame
            args, args_paramname, kwargs_paramname, values = inspect.getargvalues(
                parentframe)

        
            # show formal parameters
            for i in (args if args is not None else []):
                parameterList = parameterList +"\t{}={}".format(i, values[i])
        

            # show positional varargs
            if args_paramname is not None:
                varglist = values[args_paramname]
                for v in (varglist if varglist is not None else []):
                    parameterList = parameterList + "\t*{}={}".format(args_paramname, v)

            # show named varargs
            if kwargs_paramname is not None:
                varglist = values[kwargs_paramname]
                for k in (sorted(varglist) if varglist is not None else []):
                    parameterList = parameterList + "\t*{} {}={}".format(kwargs_paramname, k, varglist[k])

        else:
            if __name__ in stack[1][0].f_locals:
              functionCallFromSubModule = stack[1][0].f_locals["__name__"] 
            else:
                functionCallFromMethod = stack[1][3]
                methodcall = stack[3][4][0].split('.')
                



        # call line.
        line = parentframe.f_lineno

        # Remove reference to frame
        del parentframe

        def record_factoryResultException(*args, **kwargs):
            record = old_factoryResultExp(*args, **kwargs)
            record.CMRTimeStamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S,%f')[:-3]
            record.CMRSubModule = functionCallFromSubModule
            record.CMRMethod = functionCallFromMethod
            record.CMRMethodInput = parameterList
            record.CMRMethodOutput = resultDump
            record.CMRExceptionType = exceptionType
            record.CMRMethodExecutionDuration = 0
            record.CMRErrorMessage = ""
            record.CMRStackTrace = ""

            setCustomeAttributesInLogRecord(record)
            return record
        
        def setCustomeAttributesInLogRecord(record):
            record.CMRBatchId = cmrlogger.cmrLoggingOtherInfo.batchId
            record.CMRFileId = cmrlogger.cmrLoggingOtherInfo.fileId
            record.CMRProcessedFileName = cmrlogger.cmrLoggingOtherInfo.exactFileName
            record.CMRFieldId = cmrlogger.cmrLoggingOtherInfo.fieldId
            record.CMRFieldName = cmrlogger.cmrLoggingOtherInfo.fieldName
            record.CMRUserID = cmrlogger.cmrLoggingOtherInfo.userId
            record.CMRClientId = cmrlogger.cmrLoggingOtherInfo.clientId

        logging.setLogRecordFactory(record_factoryResultException)  

         #Add each handler to the Logger object
        # 'adding handlers- '
        # allows to add only one instance of file handler and stream handler
        errHandler, stdoutHandler = GetLoggingHandlers(moduleName)
        AddLoggingHandlers(cmrlogger, errHandler, stdoutHandler)
        # 'added handlers for the first time'
        fmt = SetInfoJsonFormatter()
        stdoutHandler.setFormatter(fmt)
        errHandler.setFormatter(fmt)
              
        cmrlogger.info(infoMessage) 

def get_default_logger():
    logger = CMRLoggerHandler().get_logger()
    logger.cmrLoggingOtherInfo = CMRLoggingOtherInfo()
    return logger

def format_exception(e):
    exception_list = traceback.format_stack()
    exception_list = exception_list[:-2]
    exception_list.extend(traceback.format_tb(sys.exc_info()[2]))
    exception_list.extend(traceback.format_exception_only(sys.exc_info()[0], sys.exc_info()[1]))
    exception_str = "Traceback (most recent call last):|"
    exception_str += "".join(exception_list)
     # Removing the last Pipe | symbol
    exception_str = exception_str[:-1]
    return exception_str

def log(_func=None, *, loggerHandler: Union[CMRLoggerHandler, logging.Logger] = None):
    def decorator_log(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            logger = get_default_logger()
            start = time.time()
            
            functionCallFromSubModule =""
            functionCallFromMethod =""
            parameterList =""
            result = None
            
            #try:
            if loggerHandler is None:
                first_args = next(iter(args), None)  # capture first arg to check for `self`
                logger_params = [  # does kwargs have any logger
                    x
                    for x in kwargs.values()
                    if isinstance(x, logging.Logger) or isinstance(x, CMRLoggerHandler)
                ] + [  # # does args have any logger
                    x
                    for x in args
                    if isinstance(x, logging.Logger) or isinstance(x, CMRLoggerHandler)
                ]
                if hasattr(first_args, "__dict__"):  # is first argument `self`
                    logger_params = logger_params + [
                        x
                        for x in first_args.__dict__.values()  # does class (dict) members have any logger
                        if isinstance(x, logging.Logger)
                        or isinstance(x, CMRLoggerHandler)
                    ]
                h_logger = next(iter(logger_params), CMRLoggerHandler())  # get the next/first/default logger
            else:
                h_logger = loggerHandler  # logger is passed explicitly to the decorator

            all_stack_frames = inspect.stack()
            path = Path(all_stack_frames[1].filename)
            filename_without_ext = path.stem
            moduleName = filename_without_ext

            if isinstance(h_logger, CMRLoggerHandler):
                logger = h_logger.get_logger(moduleName)
                #print("fileId in logger is",logger.cmrLoggingOtherInfo.fileId)
            else:
                logger = h_logger

            args_repr = [repr(a) for a in args]
            kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]

            try:
                if(len(args)==1 and hasattr(args[0],"__dict__")):
                    try:
                      parameterList =  json.dumps(args[0].__dict__)
                    except:
                      parameterList ="Parameter type is "+ str(type(args[0]))
                      pass  
                else:
                    parameterList = ", ".join(args_repr + kwargs_repr)
            except:
                   parameterList = ""
                   pass     

            functionCallFromMethod = func.__name__
            classMethodNames = func.__qualname__.split('.')
            
            if len(classMethodNames) == 1:
                    functionCallFromMethod = classMethodNames[0]
                    functionCallFromSubModule = ""
            elif len(classMethodNames) == 2:     
                    functionCallFromSubModule = classMethodNames[0]
                    functionCallFromMethod = classMethodNames[1]
            else:
                functionCallFromSubModule =func.__module__

            debugMessage  = functionCallFromMethod + " method Execution Started."

            if not hasattr(logger, "cmrLoggingOtherInfo"):
                logger.cmrLoggingOtherInfo = CMRLoggingOtherInfo()
            elif logger.cmrLoggingOtherInfo is None:
                logger.cmrLoggingOtherInfo = CMRLoggingOtherInfo()   

            old_factory = logging.getLogRecordFactory()

            def record_factory(*args, **kwargs):
                record = old_factory(*args, **kwargs)
                record.CMRTimeStamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S,%f')[:-3]
                record.CMRSubModule = functionCallFromSubModule
                record.CMRMethod = functionCallFromMethod
                record.CMRMethodInput = parameterList
                record.CMRExceptionType = ""
                record.CMRErrorMessage = ""
                record.CMRStackTrace = ""
                record.CMRMethodExecutionDuration = 0
                record.CMRMethodOutput =""
                setCustomeAttributesInLogRecord(record)
                return record

            def setCustomeAttributesInLogRecord(record):
                record.CMRBatchId = logger.cmrLoggingOtherInfo.batchId
                record.CMRFileId = logger.cmrLoggingOtherInfo.fileId
                record.CMRProcessedFileName = logger.cmrLoggingOtherInfo.exactFileName
                record.CMRFieldId = logger.cmrLoggingOtherInfo.fieldId
                record.CMRFieldName = logger.cmrLoggingOtherInfo.fieldName
                record.CMRUserID = logger.cmrLoggingOtherInfo.userId
                record.CMRClientId = logger.cmrLoggingOtherInfo.clientId
                
            logging.setLogRecordFactory(record_factory)
            
            errHandler, stdoutHandler = GetLoggingHandlers(moduleName)

            # Add each handler to the Logger object
            # 'adding handlers- '
            # allows to add only one instance of file handler and stream handler
            AddLoggingHandlers(logger, errHandler, stdoutHandler)
                # 'added handlers for the first time'

            logger.debug(debugMessage)
            #except Exception:
                #pass
            resultDump = None

            if not hasattr(logger, "cmrLoggingOtherInfo"):
                logger.cmrLoggingOtherInfo = CMRLoggingOtherInfo()
            elif logger.cmrLoggingOtherInfo is None:
                logger.cmrLoggingOtherInfo = CMRLoggingOtherInfo()   
            try:
                result = func(*args, **kwargs)
                resultType = str(type(result))
                print("result type is " + resultType)
                typestringList = ["str", "int", "float", "complex", "list", "tuple", "dict", "set"]
                try:
                    if not any(x in resultType for x in typestringList) and hasattr(result,"__dict__") :
                        if(resultType == "<class 'pandas.core.frame.DataFrame'>"
                        or "DataFrame" in resultType):
                            resultDump = result.to_json()
                        elif(resultType == "<class 'spacy.lang.en.English'>"):    
                            resultDump = "result type is " + resultType
                        else:    
                            try:
                                resultDump = json.dumps(result.__dict__)
                            except:
                                resultDump = "result type is " + resultType
                                pass     
                    elif(resultType == "<class 'generator'>" and not result.gi_frame is None
                    and not result.gi_frame.f_locals is None):
                        resultDump = json.dumps (result.gi_frame.f_locals)    
                    elif(resultType == "<class 'spacy.tokens.doc.Doc'>"):    
                            resultDump = result.to_json()      
                    elif(resultType == "<class 'numpy.ndarray'>"):    
                            resultDump =  json.dumps(result.tolist())               
                    else:
                        resultDump = json.dumps(result)
                except Exception as einner:
                        resultDump = "result type is " + resultType
                        pass     
                end = time.time()
                duration = f"{end-start}"                    
                debugMessage  = functionCallFromMethod + " method Execution Successfully Completed." 
                old_factoryResult = logging.getLogRecordFactory()

                def record_factoryResult(*args, **kwargs):
                    record = old_factoryResult(*args, **kwargs)
                    record.CMRTimeStamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S,%f')[:-3]
                    record.CMRSubModule = functionCallFromSubModule
                    record.CMRMethod = functionCallFromMethod
                    record.CMRMethodInput = parameterList
                    record.CMRMethodOutput = resultDump
                    record.CMRExceptionType = ""
                    record.CMRMethodExecutionDuration = duration
                    record.CMRErrorMessage = ""
                    record.CMRStackTrace = ""
                    setCustomeAttributesInLogRecord(record)
                    return record
                
                logging.setLogRecordFactory(record_factoryResult)

                fmt = SetInfoJsonFormatter()
                stdoutHandler.setFormatter(fmt)
                errHandler.setFormatter(fmt)

                logger.info(debugMessage)

            except Exception as e:
                end = time.time()
                duration = f"{end-start}"
                exceptionType = e.__class__.__name__
                exceptionMessage = str(e)
                execStackTrace = format_exception(e)
                old_factoryResultExp = logging.getLogRecordFactory()

                def record_factoryResultException(*args, **kwargs):
                    record = old_factoryResultExp(*args, **kwargs)
                    record.CMRTimeStamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S,%f')[:-3]
                    record.CMRSubModule = functionCallFromSubModule
                    record.CMRMethod = functionCallFromMethod
                    record.CMRMethodInput = parameterList
                    record.CMRMethodOutput = resultDump
                    record.CMRExceptionType = exceptionType
                    record.CMRMethodExecutionDuration = duration
                    record.CMRErrorMessage = exceptionMessage
                    record.CMRStackTrace = execStackTrace
                    setCustomeAttributesInLogRecord(record)
                    return record
                
                logging.setLogRecordFactory(record_factoryResultException)

                  # Set the log format on each handler
                fmt = SetErrorJSONFormatter()
                stdoutHandler.setFormatter(fmt)
                errHandler.setFormatter(fmt)
                logger.error(functionCallFromMethod +" failed due to error.", exc_info=False)
                #todo: uncomment below line after testing
                raise e
            finally:
                end = time.time()
                duration = f"{end-start}"

                fmt = SetDebugJsonFormatter()
                stdoutHandler.setFormatter(fmt)
                errHandler.setFormatter(fmt)

                old_factoryFinal = logging.getLogRecordFactory()

                def record_factoryFinal(*args, **kwargs):
                    record = old_factoryFinal(*args, **kwargs)
                    record.CMRTimeStamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S,%f')[:-3]
                    record.CMRSubModule = functionCallFromSubModule
                    record.CMRMethod = functionCallFromMethod
                    record.CMRMethodInput = parameterList
                    record.CMRMethodOutput = resultDump
                    record.CMRExceptionType = ""
                    record.CMRErrorMessage = ""
                    record.CMRStackTrace = ""
                    record.CMRMethodExecutionDuration = duration                    
                    setCustomeAttributesInLogRecord(record)
                    return record
                
                logging.setLogRecordFactory(record_factoryFinal)
                debugMessage  = functionCallFromMethod + " method Execution ended."
                logger.debug(debugMessage)
                return result
        return wrapper

    if _func is None:
        return decorator_log
    else:
        return decorator_log(_func)
    
def SetDebugJsonFormatter():
    fmt = JSONLogger.JsonFormatter(
            "%(name)s %(asctime)s %(levelname)s %(filename)s %(lineno)s %(process)d %(message)s %(taskName)s %(lineno)d",
            rename_fields={"asctime": "CMRLoggerTimeStamp","levelname": "CMRLOGLEVEL","message":"CMRLogMessage",
                    "name":"CMRModule","filename": "CMRFileName","lineno":"CMRLineNo","process":"CMRProcessId","taskName":"CMRTaskName"},
        )
        
    return fmt

def SetInfoJsonFormatter():
    fmt = JSONLogger.JsonFormatter(
            "%(name)s %(asctime)s %(levelname)s %(filename)s %(lineno)s %(process)d %(message)s %(taskName)s %(lineno)d",
            rename_fields={"asctime": "CMRLoggerTimeStamp","levelname": "CMRLOGLEVEL","message":"CMRLogMessage",
                    "name":"CMRModule","filename": "CMRFileName","lineno":"CMRLineNo","process":"CMRProcessId","taskName":"CMRTaskName"},
        )
        
    return fmt

def SetErrorJSONFormatter():
    fmt = JSONLogger.JsonFormatter(
        "%(name)s %(asctime)s %(levelname)s %(filename)s %(lineno)s %(process)d %(message)s %(taskName)s",
            rename_fields={"asctime": "CMRLoggerTimeStamp","levelname": "CMRLOGLEVEL","message":"CMRLogMessage",
                    "name":"CMRModule","filename": "CMRFileName",
                    "lineno":"CMRLineNo","process":"CMRProcessId","taskName":"CMRTaskName"}
                    )
                
    return fmt

def SetWarnJsonFormatter():
    fmt = JSONLogger.JsonFormatter(
            "%(name)s %(asctime)s %(levelname)s %(filename)s %(lineno)s %(process)d %(message)s %(taskName)s %(lineno)d",
            rename_fields={"asctime": "CMRLoggerTimeStamp","levelname": "CMRLOGLEVEL","message":"CMRLogMessage",
                    "name":"CMRModule","filename": "CMRFileName","lineno":"CMRLineNo","process":"CMRProcessId","taskName":"CMRTaskName"},
        )
        
    return fmt

def AddLoggingHandlers(logger, errHandler, stdoutHandler):
    if len(logger.handlers) > 0:
            # 'making sure we do not add duplicate handlers'
        for handler in logger.handlers:
                # add the handlers to the logger
                # makes sure no duplicate handlers are added
            if not isinstance(handler, logging.FileHandler) and not isinstance(handler, logging.StreamHandler):
                    logger.addHandler(stdoutHandler)
                        # 'added file handler'
                    logger.addHandler(errHandler)
                        # 'added stream handler'
    else:
        logger.addHandler(stdoutHandler)
        logger.addHandler(errHandler)

def GetLoggingHandlers(moduleName):
    timestr = time.strftime("%d-%m-%Y")
    
   # current_working_directory = os.getcwd()
    current_working_directory, currentfilename = os.path.split(os.path.abspath(__file__))
    logPath = current_working_directory+"\\logs\\"
    isExist = os.path.exists(logPath)
    if not isExist:
       # Create a new directory because it does not exist
        os.makedirs(logPath)
    fileName = os.path.join(logPath, moduleName + timestr + ".log")
    errHandler = logging.FileHandler(fileName)
        # Create handlers for logging to the standard output and a file
    stdoutHandler = logging.StreamHandler(stream=sys.stdout)
        # Set the log levels on the handlers
    stdoutHandler.setLevel(logging.DEBUG)
    errHandler.setLevel(logging.DEBUG)
   # stdoutHandler.propagate = False
   # logging.StreamHandler(stream=None)
    fmt = SetDebugJsonFormatter()
        # Set the log format on each handler
    stdoutHandler.setFormatter(fmt)
    errHandler.setFormatter(fmt)
    return errHandler,stdoutHandler
