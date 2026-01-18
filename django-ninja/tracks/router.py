from ninja import Router
from django.shortcuts import get_object_or_404

from tracks.models import Track
from tracks.schemas import TrackSchema, NotFoundSchema

router = Router()

@router.get("/tracks", response={200: list[TrackSchema]})
def get_tracks(request):
    return Track.objects.all()

@router.get("/tracks/{track_id}", response={200: TrackSchema, 404: NotFoundSchema})
def get_track_by_id(request, track_id: int):
    track = get_object_or_404(Track, id=track_id)
    return track

@router.post("/tracks", response={201: TrackSchema})
def create_track(request, track: TrackSchema):
    track = Track.objects.create(**track.dict())
    return track

@router.put("/tracks/{track_id}", response={200: TrackSchema, 404: NotFoundSchema})
def update_track(request, track_id: int, data: TrackSchema):
    track = get_object_or_404(Track, id=track_id)
    for attribute, value in data.dict().items():
        setattr(track, attribute, value)
    track.save()
    return track

@router.delete("/tracks/{track_id}")
def delete_track(request, track_id: int):
    track = get_object_or_404(Track, id=track_id)
    track.delete()
    return 200

