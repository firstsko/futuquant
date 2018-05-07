# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Trd_GetPositionList.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import Common_pb2 as Common__pb2
import Trd_Common_pb2 as Trd__Common__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='Trd_GetPositionList.proto',
  package='Trd_GetPositionList',
  syntax='proto2',
  serialized_pb=_b('\n\x19Trd_GetPositionList.proto\x12\x13Trd_GetPositionList\x1a\x0c\x43ommon.proto\x1a\x10Trd_Common.proto\"\x9b\x01\n\x03\x43\x32S\x12%\n\x06header\x18\x01 \x02(\x0b\x32\x15.Trd_Common.TrdHeader\x12\x39\n\x10\x66ilterConditions\x18\x02 \x01(\x0b\x32\x1f.Trd_Common.TrdFilterConditions\x12\x18\n\x10\x66ilterPLRatioMin\x18\x03 \x01(\x01\x12\x18\n\x10\x66ilterPLRatioMax\x18\x04 \x01(\x01\"X\n\x03S2C\x12%\n\x06header\x18\x01 \x02(\x0b\x32\x15.Trd_Common.TrdHeader\x12*\n\x0cpositionList\x18\x02 \x03(\x0b\x32\x14.Trd_Common.Position\"0\n\x07Request\x12%\n\x03\x63\x32s\x18\x01 \x02(\x0b\x32\x18.Trd_GetPositionList.C2S\"i\n\x08Response\x12\x15\n\x07retType\x18\x01 \x02(\x05:\x04-400\x12\x0e\n\x06retMsg\x18\x02 \x01(\t\x12\x0f\n\x07\x65rrCode\x18\x03 \x01(\x05\x12%\n\x03s2c\x18\x04 \x01(\x0b\x32\x18.Trd_GetPositionList.S2C')
  ,
  dependencies=[Common__pb2.DESCRIPTOR,Trd__Common__pb2.DESCRIPTOR,])




_C2S = _descriptor.Descriptor(
  name='C2S',
  full_name='Trd_GetPositionList.C2S',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='Trd_GetPositionList.C2S.header', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='filterConditions', full_name='Trd_GetPositionList.C2S.filterConditions', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='filterPLRatioMin', full_name='Trd_GetPositionList.C2S.filterPLRatioMin', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='filterPLRatioMax', full_name='Trd_GetPositionList.C2S.filterPLRatioMax', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=83,
  serialized_end=238,
)


_S2C = _descriptor.Descriptor(
  name='S2C',
  full_name='Trd_GetPositionList.S2C',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='Trd_GetPositionList.S2C.header', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='positionList', full_name='Trd_GetPositionList.S2C.positionList', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=240,
  serialized_end=328,
)


_REQUEST = _descriptor.Descriptor(
  name='Request',
  full_name='Trd_GetPositionList.Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='c2s', full_name='Trd_GetPositionList.Request.c2s', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=330,
  serialized_end=378,
)


_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='Trd_GetPositionList.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='retType', full_name='Trd_GetPositionList.Response.retType', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=True, default_value=-400,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='retMsg', full_name='Trd_GetPositionList.Response.retMsg', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='errCode', full_name='Trd_GetPositionList.Response.errCode', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='s2c', full_name='Trd_GetPositionList.Response.s2c', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=380,
  serialized_end=485,
)

_C2S.fields_by_name['header'].message_type = Trd__Common__pb2._TRDHEADER
_C2S.fields_by_name['filterConditions'].message_type = Trd__Common__pb2._TRDFILTERCONDITIONS
_S2C.fields_by_name['header'].message_type = Trd__Common__pb2._TRDHEADER
_S2C.fields_by_name['positionList'].message_type = Trd__Common__pb2._POSITION
_REQUEST.fields_by_name['c2s'].message_type = _C2S
_RESPONSE.fields_by_name['s2c'].message_type = _S2C
DESCRIPTOR.message_types_by_name['C2S'] = _C2S
DESCRIPTOR.message_types_by_name['S2C'] = _S2C
DESCRIPTOR.message_types_by_name['Request'] = _REQUEST
DESCRIPTOR.message_types_by_name['Response'] = _RESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

C2S = _reflection.GeneratedProtocolMessageType('C2S', (_message.Message,), dict(
  DESCRIPTOR = _C2S,
  __module__ = 'Trd_GetPositionList_pb2'
  # @@protoc_insertion_point(class_scope:Trd_GetPositionList.C2S)
  ))
_sym_db.RegisterMessage(C2S)

S2C = _reflection.GeneratedProtocolMessageType('S2C', (_message.Message,), dict(
  DESCRIPTOR = _S2C,
  __module__ = 'Trd_GetPositionList_pb2'
  # @@protoc_insertion_point(class_scope:Trd_GetPositionList.S2C)
  ))
_sym_db.RegisterMessage(S2C)

Request = _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), dict(
  DESCRIPTOR = _REQUEST,
  __module__ = 'Trd_GetPositionList_pb2'
  # @@protoc_insertion_point(class_scope:Trd_GetPositionList.Request)
  ))
_sym_db.RegisterMessage(Request)

Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), dict(
  DESCRIPTOR = _RESPONSE,
  __module__ = 'Trd_GetPositionList_pb2'
  # @@protoc_insertion_point(class_scope:Trd_GetPositionList.Response)
  ))
_sym_db.RegisterMessage(Response)


# @@protoc_insertion_point(module_scope)