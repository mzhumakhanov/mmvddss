# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: SetLabelParams.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='SetLabelParams.proto',
  package='qlua.rpc.SetLabelParams',
  syntax='proto3',
  serialized_options=_b('\n\010qlua.rpcH\001'),
  serialized_pb=_b('\n\x14SetLabelParams.proto\x12\x17qlua.rpc.SetLabelParams\"\xab\x01\n\x07Request\x12\x11\n\tchart_tag\x18\x01 \x01(\t\x12\x10\n\x08label_id\x18\x02 \x01(\x05\x12G\n\x0clabel_params\x18\x03 \x03(\x0b\x32\x31.qlua.rpc.SetLabelParams.Request.LabelParamsEntry\x1a\x32\n\x10LabelParamsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x18\n\x06Result\x12\x0e\n\x06result\x18\x01 \x01(\x08\x42\x0c\n\x08qlua.rpcH\x01\x62\x06proto3')
)




_REQUEST_LABELPARAMSENTRY = _descriptor.Descriptor(
  name='LabelParamsEntry',
  full_name='qlua.rpc.SetLabelParams.Request.LabelParamsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='qlua.rpc.SetLabelParams.Request.LabelParamsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='qlua.rpc.SetLabelParams.Request.LabelParamsEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=171,
  serialized_end=221,
)

_REQUEST = _descriptor.Descriptor(
  name='Request',
  full_name='qlua.rpc.SetLabelParams.Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='chart_tag', full_name='qlua.rpc.SetLabelParams.Request.chart_tag', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='label_id', full_name='qlua.rpc.SetLabelParams.Request.label_id', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='label_params', full_name='qlua.rpc.SetLabelParams.Request.label_params', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_REQUEST_LABELPARAMSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=50,
  serialized_end=221,
)


_RESULT = _descriptor.Descriptor(
  name='Result',
  full_name='qlua.rpc.SetLabelParams.Result',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='qlua.rpc.SetLabelParams.Result.result', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=223,
  serialized_end=247,
)

_REQUEST_LABELPARAMSENTRY.containing_type = _REQUEST
_REQUEST.fields_by_name['label_params'].message_type = _REQUEST_LABELPARAMSENTRY
DESCRIPTOR.message_types_by_name['Request'] = _REQUEST
DESCRIPTOR.message_types_by_name['Result'] = _RESULT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Request = _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), dict(

  LabelParamsEntry = _reflection.GeneratedProtocolMessageType('LabelParamsEntry', (_message.Message,), dict(
    DESCRIPTOR = _REQUEST_LABELPARAMSENTRY,
    __module__ = 'SetLabelParams_pb2'
    # @@protoc_insertion_point(class_scope:qlua.rpc.SetLabelParams.Request.LabelParamsEntry)
    ))
  ,
  DESCRIPTOR = _REQUEST,
  __module__ = 'SetLabelParams_pb2'
  # @@protoc_insertion_point(class_scope:qlua.rpc.SetLabelParams.Request)
  ))
_sym_db.RegisterMessage(Request)
_sym_db.RegisterMessage(Request.LabelParamsEntry)

Result = _reflection.GeneratedProtocolMessageType('Result', (_message.Message,), dict(
  DESCRIPTOR = _RESULT,
  __module__ = 'SetLabelParams_pb2'
  # @@protoc_insertion_point(class_scope:qlua.rpc.SetLabelParams.Result)
  ))
_sym_db.RegisterMessage(Result)


DESCRIPTOR._options = None
_REQUEST_LABELPARAMSENTRY._options = None
# @@protoc_insertion_point(module_scope)
