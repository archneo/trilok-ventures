{{- define "rag-gateway.fullname" -}}
{{- printf "%s-%s" .Release.Name "rag-gateway" | trunc 63 | trimSuffix "-" -}}
{{- end -}}
