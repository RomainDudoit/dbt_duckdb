{% test not_empty_string(model, column_name) %}
    {{ 
        config(
            severity = 'error') 
    }}
    
    select {{ column_name }} from {{ model }} where {{ column_name }} = ''
{% endtest %}
