package rag.access

default allow := false

allow if input.user.role == "analyst"
