# test_event_systems.py

import pytest
from event_systems import register_event, dispatch, events

# Dummy function for testing
def dummy_handler(data):
    dummy_handler.called = True
    dummy_handler.received = data

def test_register_event_adds_handler():
    events.clear()  # Clear before test
    register_event('test_event', dummy_handler)
    assert 'test_event' in events
    assert dummy_handler in events['test_event']

def test_dispatch_calls_handler():
    events.clear()
    dummy_handler.called = False
    dummy_handler.received = None

    register_event('test_event', dummy_handler)
    dispatch('test_event', 'hello')
    
    assert dummy_handler.called
    assert dummy_handler.received == 'hello'

def test_dispatch_with_no_handlers():
    events.clear()
    with pytest.raises(ValueError):
        dispatch('nonexistent_event', 'test')
