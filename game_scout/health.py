from django.db import connections
from django.http import JsonResponse


def live(request):
    return JsonResponse({"status": "ok", "service": "game-scout-api"})


def ready(request):
    try:
        with connections["default"].cursor() as cursor:
            cursor.execute("SELECT 1")
            cursor.fetchone()
    except Exception as exc:  # pragma: no cover - defensive fallback
        return JsonResponse(
            {"status": "error", "detail": str(exc)},
            status=503,
        )
    return JsonResponse({"status": "ready"})
