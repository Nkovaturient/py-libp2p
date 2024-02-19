# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: libp2p/identity/identify/pb/identify.proto

import sys

_b = sys.version_info[0] < 3 and (lambda x: x) or (lambda x: x.encode("latin1"))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor.FileDescriptor(
    name="libp2p/identity/identify/pb/identify.proto",
    package="identify.pb",
    syntax="proto2",
    serialized_options=None,
    serialized_pb=_b(
        '\n*libp2p/identity/identify/pb/identify.proto\x12\x0bidentify.pb"\x8f\x01\n\x08Identify\x12\x18\n\x10protocol_version\x18\x05 \x01(\t\x12\x15\n\ragent_version\x18\x06 \x01(\t\x12\x12\n\npublic_key\x18\x01 \x01(\x0c\x12\x14\n\x0clisten_addrs\x18\x02 \x03(\x0c\x12\x15\n\robserved_addr\x18\x04 \x01(\x0c\x12\x11\n\tprotocols\x18\x03 \x03(\t'
    ),
)


_IDENTIFY = _descriptor.Descriptor(
    name="Identify",
    full_name="identify.pb.Identify",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="protocol_version",
            full_name="identify.pb.Identify.protocol_version",
            index=0,
            number=5,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="agent_version",
            full_name="identify.pb.Identify.agent_version",
            index=1,
            number=6,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="public_key",
            full_name="identify.pb.Identify.public_key",
            index=2,
            number=1,
            type=12,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b(""),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="listen_addrs",
            full_name="identify.pb.Identify.listen_addrs",
            index=3,
            number=2,
            type=12,
            cpp_type=9,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="observed_addr",
            full_name="identify.pb.Identify.observed_addr",
            index=4,
            number=4,
            type=12,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b(""),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="protocols",
            full_name="identify.pb.Identify.protocols",
            index=5,
            number=3,
            type=9,
            cpp_type=9,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto2",
    extension_ranges=[],
    oneofs=[],
    serialized_start=60,
    serialized_end=203,
)

DESCRIPTOR.message_types_by_name["Identify"] = _IDENTIFY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Identify = _reflection.GeneratedProtocolMessageType(
    "Identify",
    (_message.Message,),
    {
        "DESCRIPTOR": _IDENTIFY,
        "__module__": "libp2p.identity.identify.pb.identify_pb2"
        # @@protoc_insertion_point(class_scope:identify.pb.Identify)
    },
)
_sym_db.RegisterMessage(Identify)


# @@protoc_insertion_point(module_scope)
