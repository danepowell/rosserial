# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import nanopb_pb2

DESCRIPTOR = descriptor.FileDescriptor(
  name='rosserial_msg.proto',
  package='',
  serialized_pb='\n\x13rosserial_msg.proto\x1a\x0cnanopb.proto\"~\n\rrosserial_msg\x12\x10\n\x08topic_id\x18\x01 \x02(\x05\x12\x19\n\ntopic_name\x18\x02 \x02(\tB\x05\x92?\x02\x08 \x12\x1b\n\x0cmessage_type\x18\x03 \x02(\tB\x05\x92?\x02\x08 \x12\x0c\n\x04\x64\x61ta\x18\x04 \x02(\x01\x12\x15\n\x06md5sum\x18\x05 \x02(\tB\x05\x92?\x02\x08@')




_ROSSERIAL_MSG = descriptor.Descriptor(
  name='rosserial_msg',
  full_name='rosserial_msg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='topic_id', full_name='rosserial_msg.topic_id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='topic_name', full_name='rosserial_msg.topic_name', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\222?\002\010 ')),
    descriptor.FieldDescriptor(
      name='message_type', full_name='rosserial_msg.message_type', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\222?\002\010 ')),
    descriptor.FieldDescriptor(
      name='data', full_name='rosserial_msg.data', index=3,
      number=4, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='md5sum', full_name='rosserial_msg.md5sum', index=4,
      number=5, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\222?\002\010@')),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=37,
  serialized_end=163,
)

DESCRIPTOR.message_types_by_name['rosserial_msg'] = _ROSSERIAL_MSG

class rosserial_msg(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _ROSSERIAL_MSG
  
  # @@protoc_insertion_point(class_scope:rosserial_msg)

# @@protoc_insertion_point(module_scope)