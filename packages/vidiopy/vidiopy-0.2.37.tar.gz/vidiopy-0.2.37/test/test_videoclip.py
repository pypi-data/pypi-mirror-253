import pytest
from vidiopy.video.VideoClip import VideoClip
from PIL import Image
import numpy as np


def test_VideoClip_initialization():
    clip = VideoClip()
    assert isinstance(clip, VideoClip)
    assert clip._st == 0.0
    assert clip._ed is None
    assert clip._dur is None
    assert clip.audio is None
    assert clip.fps is None
    assert clip.size is None
    assert callable(clip.pos)
    assert clip.relative_pos is False


def test_VideoClip_repr():
    clip = VideoClip()
    assert isinstance(clip.__repr__(), str)


def test_VideoClip_str():
    clip = VideoClip()
    assert isinstance(clip.__str__(), str)


def test_VideoClip_len():
    clip = VideoClip()
    assert clip.__len__() is None


def test_VideoClip_width():
    clip = VideoClip()
    with pytest.raises(ValueError):
        clip.width


def test_VideoClip_height():
    clip = VideoClip()
    with pytest.raises(ValueError):
        clip.height


def test_VideoClip_aspect_ratio():
    clip = VideoClip()
    with pytest.raises(ValueError):
        clip.aspect_ratio


def test_VideoClip_start():
    clip = VideoClip()
    assert clip.start == 0.0


def test_VideoClip_end():
    clip = VideoClip()
    assert clip.end is None


def test_VideoClip_duration():
    clip = VideoClip()
    assert clip.duration is None


def test_VideoClip_set_position():
    clip = VideoClip()
    with pytest.raises(TypeError):
        clip.set_position("invalid")


def test_VideoClip_set_audio():
    clip = VideoClip()
    clip.set_audio(None)
    assert clip.audio is None


def test_VideoClip_set_fps():
    clip = VideoClip()
    clip.set_fps(30)
    assert clip.fps == 30


def test_VideoClip_without_audio():
    clip = VideoClip()
    clip.without_audio()
    assert clip.audio is None


def test_VideoClip_copy():
    clip = VideoClip()
    copied_clip = clip.copy()
    assert copied_clip is not clip
    assert copied_clip.__dict__ == clip.__dict__


def test_VideoClip_set_start():
    clip = VideoClip()
    clip.set_start(10)
    assert clip.start == 10


def test_VideoClip_set_end():
    clip = VideoClip()
    clip.set_end(20)
    assert clip.end == 20


def test_VideoClip_set_duration():
    clip = VideoClip()
    clip.set_duration(30)
    assert clip.duration == 30


def test_make_frame_array():
    clip = VideoClip()
    with pytest.raises(NotImplementedError):
        clip.make_frame_array(0)


def test_make_frame_pil():
    clip = VideoClip()
    with pytest.raises(NotImplementedError):
        clip.make_frame_pil(0)


def test_get_frame():
    video_clip = VideoClip()

    # Mocking the methods that get_frame depends on
    video_clip.make_frame_array = lambda t: np.array([t])
    video_clip.make_frame_pil = lambda t: Image.new('RGB', (t, t))

    t = 10

    # Test when is_pil is None or False
    frame = video_clip.get_frame(t)
    assert isinstance(frame, np.ndarray)
    assert frame[0] == t

    # Test when is_pil is True
    frame = video_clip.get_frame(t, is_pil=True)
    assert isinstance(frame, Image.Image)
    assert frame.size == (t, t)

    # Test when is_pil is an unexpected value
    with pytest.raises(ValueError):
        video_clip.get_frame(t, is_pil='unexpected')


def test_iterate_frames_pil_t():
    # Create a VideoClip instance
    video_clip = VideoClip()

    # Mocking the methods that get_frame depends on
    video_clip.make_frame_pil = lambda t: Image.new('RGB', (t, t))

    for t, frame in enumerate(video_clip.iterate_frames_pil_t(2)):
        assert isinstance(frame, Image.Image)
        assert frame.size == (t, t)
        assert frame.mode == 'RGB'


def test_iterate_frames_array_t():
    # Create a VideoClip instance
    video_clip = VideoClip()

    # Mocking the methods that get_frame depends on
    video_clip.make_frame_array = lambda t: np.array([t])

    for t, frame in enumerate(video_clip.iterate_frames_array_t(2)):
        assert isinstance(frame, np.ndarray)
        assert frame[0] == t


def test_sub_clip_copy():
    clip = VideoClip()
    with pytest.raises(NotImplementedError):
        clip.sub_clip_copy()


def test_sub_clip():
    clip = VideoClip()
    with pytest.raises(NotImplementedError):
        clip.sub_clip()


def test_fl_frame_transform():
    clip = VideoClip()
    with pytest.raises(NotImplementedError):
        clip.fl_frame_transform(lambda x: x)


def test_fl_clip_transform():
    clip = VideoClip()
    with pytest.raises(NotImplementedError):
        clip.fl_clip_transform(lambda x: x)


def test_fl_time_transform():
    clip = VideoClip()
    # Mocking the methods that get_frame depends on
    clip.make_frame_array = lambda t: np.array([t])
    original_make_frame_array_t = clip.make_frame_array
    clip.make_frame_pil = lambda t: Image.new('RGB', (t, t))
    original_make_frame_pil_t = clip.make_frame_pil
    original_get_frame = clip.get_frame
    clip.fl_time_transform(lambda t: t+1)

    # Check that the original methods are not changed
    assert clip.make_frame_array == original_make_frame_array_t
    assert clip.make_frame_pil == original_make_frame_pil_t
    assert clip.get_frame == original_get_frame

    # Check that the new methods are changed
    assert clip.make_frame_array(1)[0] == 2
    assert clip.make_frame_pil(1).size == (2, 2)
    assert clip.get_frame(1)[0] == 2
    assert clip.get_frame(1, is_pil=True).size == (2, 2)

