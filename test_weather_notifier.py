from unittest.mock import patch
import weather_notifier  # Your script with get_weather() and send_email()

@patch('weather_notifier.requests.get')
def test_get_weather_success(mock_get):
    # Simulate a successful API response
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        "weather": [{"main": "Rain"}],
        "main": {"temp": 10}
    }

    weather, temp = weather_notifier.get_weather()
    assert weather == "Rain"
    assert temp == 10

@patch('weather_notifier.yagmail.SMTP')
def test_send_email_success(mock_yag):
    # Simulate email sending
    instance = mock_yag.return_value
    weather_notifier.send_email("Test Subject", "Test Message")
    instance.send.assert_called_once()

