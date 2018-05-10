from rest_framework import renderers


class CustomJsonRenderer(renderers.JSONRenderer):

    def render(self, data, accepted_media_type=None, renderer_context=None):

        if renderer_context:
            print(data)
            if isinstance(data, dict):
                status = msg = data.pop('msg', '请求成功')
                desc = code = data.pop('code', 200)
            else:
                if data:
                    status = code = 900
                    desc = msg = '用户名已存在'
                else:
                    status = code = 200
                    desc = msg = '用户名可用'

            response = renderer_context['response']
            response.status_code = 200
            res = {
                'code': code,
                'msg': msg,
                'desc': desc,
                'status': status,
            }

            return super().render(res, accepted_media_type, renderer_context)

        else:

            return super().render(data, accepted_media_type, renderer_context)
