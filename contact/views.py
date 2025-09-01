from rest_framework import viewsets, permissions, status
from rest_framework.response import Response

from django.conf import settings
from django.core.mail import EmailMessage, mail_admins

from .models import ContactMessage
from .serializers import ContactMessageSerializer


class IsAdminOrCreateOnly(permissions.BasePermission):
    """
    - Oricine poate face POST (create)
    - Doar staff/admin poate lista / vedea / modifica / șterge
    """
    def has_permission(self, request, view):
        if request.method == "POST":
            return True
        return bool(request.user and request.user.is_staff)


class ContactMessageViewSet(viewsets.ModelViewSet):
    queryset = ContactMessage.objects.all()
    serializer_class = ContactMessageSerializer
    permission_classes = [IsAdminOrCreateOnly]

    def create(self, request, *args, **kwargs):
        payload = request.data.copy()
        for key in ("name", "email", "phone", "subject", "message"):
            if key in payload and isinstance(payload.get(key), str):
                payload[key] = payload[key].strip()

        serializer = self.get_serializer(data=payload)
        serializer.is_valid(raise_exception=True)

        self.perform_create(serializer)
        obj = serializer.instance

        subject = f"[Contact] {obj.name} — {obj.subject or 'Mesaj nou'}"
        body = (
            f"Nume: {obj.name}\n"
            f"Email: {obj.email}\n"
            f"Telefon: {obj.phone or '-'}\n"
            f"Subiect: {obj.subject or '-'}\n\n"
            f"Mesaj:\n{obj.message}\n"
        )

        try:
            to_list = getattr(settings, "CONTACT_TO_EMAILS", [])
            if to_list:
                email = EmailMessage(
                    subject=subject,
                    body=body,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    to=to_list,
                    headers={"Reply-To": obj.email} if obj.email else None,
                )
                email.send(fail_silently=False)
        except Exception as e:
            
            print("Eroare trimitere către CONTACT_TO_EMAILS:", e)

        try:
            mail_admins(subject=subject, message=body, fail_silently=True)
        except Exception:
            pass

        return Response(
            {"detail": "Mesajul a fost salvat și e-mailul a fost trimis. Îți mulțumim!", "id": obj.id},
            status=status.HTTP_201_CREATED, 
        )
