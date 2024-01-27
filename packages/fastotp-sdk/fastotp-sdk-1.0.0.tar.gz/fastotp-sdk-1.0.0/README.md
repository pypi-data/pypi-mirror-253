# FastOtp

The FastOTP Wrapper SDK is designed to simplify the integration and usage of the FastOTP service in Python applications. FastOTP is a service that provides functionality for generating, validating, and delivering One-Time Passwords (OTPs) through various channels.

## Installation

To install PyResponse, you can use pip:

```bash
pip install fastotp
```

## Usage

Fastotp can be used with different web frameworks, including Django, FastAPI, and Flask. Here's how you can use Fastotp in each framework:

### # Example usage

```python
from fastotp_sdk.client import FastOTPClient, TokenType
```

## Initialize FastOTP client

```python
api_key = "your_api_key"
fastotp_sdk = FastOTPClient(api_key)
```

## Generate OTP

```python
generated_otp = fastotp_sdk.generate_otp(token_type=TokenType.NUMERIC, token_length=6, validity=10)
print("Generated OTP:", generated_otp)
```

## Validate OTP

```python
validation_result = fastotp_sdk.validate_otp(identifier="example_identifier", token="123456")
print("Validation Result:", validation_result)
```

## Get OTP Details

```python
otp_details = fastotp_sdk.get_otp_details(otp_id="123")
print("OTP Details:", otp_details)
```

### Django

1. Install FastOtp using pip as shown in the installation section.
2. Import the necessary functions from FastOtp in your Django views or API handlers.

```python
# In your views or models
from fastotp_sdk.client import FastOTPClient, TokenType

api_key = "your_api_key"
fastotp_sdk = FastOTPClient(api_key)

# Generate OTP
generated_otp = fastotp_sdk.generate_otp(token_type=TokenType.NUMERIC, token_length=6, validity=10)

# Use generated_otp as needed in your Django application

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
