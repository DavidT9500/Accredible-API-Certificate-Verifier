# Accredible API Certificate Verifier

![MIT License](https://img.shields.io/badge/license-MIT-green)
![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen)
![Last Commit](https://img.shields.io/github/last-commit/ryanlibs/Accredible-API-Certificate-Verifier)
![Issues](https://img.shields.io/github/issues/ryanlibs/Accredible-API-Certificate-Verifier)


## Motivation

I created this because the official INE certificate verification endpoints ([my.ine.com/certifications](https://my.ine.com/certifications/) or [my.ine.com/certificate/{credential_id}](https://my.ine.com/certificate/{credential_id})) are currently broken and return a 503 error. This makes it impossible for users, employers, or anyone else to verify INE certifications through the official site.

With this, anyone can verify INE certificates directly. If you need to confirm the validity of an INE credential and the official service is down, you can use this as a alternative.

## Features
- Verify any Accredible certificate by credential ID (not limited to INE)
- Fetch certificate details, verification status, and related events

## Usage

### API Endpoint

`GET /verify/{credential_id}`

Verifies a certificate by its credential ID. Returns certificate details, verification status, and related events.

#### Example Request

```http
GET /verify/123456
```

#### Example Response

```json
{
   "verify": true,
   "name": "John Doe",
   "certification": "INE Certified Expert",
   "description": "Awarded for passing the INE Expert exam.",
   "issued_on": "2025-08-01T00:00:00Z",
   "expires_on": "2028-08-01T00:00:00Z",
   "issuer": "INE",
   "blockchain_address": "0x123456789abcdef",
   "events": [
      {
         "type": "issued",
         "data": {"date": "2025-08-01T00:00:00Z"}
      }
   ]
}
```

### Documentation

- /docs
- /redoc


## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request if you have ideas or fixes.

## Support

If you find this API useful and want to support my caffeine addiction, please consider buying me a coffee! ☕😁

[![Buy Me a Coffee](https://img.shields.io/badge/Support-Buy%20Me%20a%20Coffee-orange?logo=buymeacoffee)](https://www.buymeacoffee.com/ryanlibs)