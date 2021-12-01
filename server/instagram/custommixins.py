from django.contrib.sessions.models import Session
from rest_framework.response import Response


class CreateAuthorization:
    def create(self, request, *args, **kwargs):
        # Allow access only to people who are currently logged in
        if request.session.session_key is not None:
            # If the image author matches the logged in user, proceed with creation
            session = Session.objects.get(session_key=request.session.session_key)
            session_data = session.get_decoded()
            uid = session_data.get('_auth_user_id')
            if uid == request.data['author']:
                serializer = self.get_serializer(data=request.data)
                serializer.is_valid(raise_exception=True)
                self.perform_create(serializer)
                headers = self.get_success_headers(serializer.data)
                return Response(serializer.data, status=201, headers=headers)
            else:
                return Response('You are not authorized to post for that user.', status=403)
        else:
            return Response('Log in to post.', status=403)
