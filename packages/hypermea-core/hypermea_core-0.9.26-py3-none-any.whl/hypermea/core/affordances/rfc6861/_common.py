def generate_hal_forms_template(method, schema, self_ref, resource=None):
    template = {'_links': {'self': {'href': self_ref}}}
    
    def process_schema(schema):
        properties = []

        for field, field_info in schema.items():
            if field.startswith('_'):
                continue

            field_type = field_info.get('type', 'string')
            hal_field = {
                'name': field,
                'prompt': f'Enter {field}',
                'required': field_info.get('required', False),
                'value': resource[field] if resource else ''
            }
            if field_type == 'dict':
                hal_field['type'] = 'object'
                hal_field['properties'] = process_schema(field_info['schema'])
            elif field_type == 'list':
                hal_field['type'] = 'array'
                hal_field['items'] = process_schema({'item': field_info['schema']['item']})
            elif field_type == 'integer':
                hal_field['type'] = 'number'
            else:    
                hal_field['type'] = field_type

            if field_info.get('allow_unknown'):
                hal_field['hyAnyObject'] = True
            else:
                if 'allowed' in field_info:
                    hal_field['options'] = {
                        'inline': field_info['allowed'],
                        'maxItems': 1
                    }
                    if 'default' in field_info:
                        hal_field['options']['selectedValues'] = [field_info['default']]
                    if field in resource:
                        hal_field['options']['selectedValues'] = [resource[field]]

                if 'min' in field_info:
                    hal_field['min'] = field_info['min']

                if 'max' in field_info:
                    hal_field['max'] = field_info['max']

                if 'maxlength' in field_info:
                    hal_field['maxLength'] = field_info['maxlength']

                if 'minlength' in field_info:
                    hal_field['minLength'] = field_info['minlength']

                if 'regex' in field_info:
                    hal_field['pattern'] = field_info['regex']

                if field_type == 'datetime':
                    hal_field['format'] = 'date-time'

            properties.append(hal_field)
        return properties

    properties = process_schema(schema)
    template['_templates'] = {
        'default': {
            'method': method,
            # 'title': 'Soon is coming',
            'contentType': 'application/json',
            'properties': properties,
        }
    }

    return template
