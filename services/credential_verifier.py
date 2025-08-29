import httpx

BASE_URL = "https://api.accredible.com/v1/credential-net/credentials"

async def verify_credential_data(credential_id: int):
    async with httpx.AsyncClient(timeout=15.0) as client:
        try:
            tx_resp = await client.get(f"{BASE_URL}/{credential_id}/blockchain_transaction")
            tx_resp.raise_for_status()
        except httpx.HTTPStatusError as e:
            if e.response.status_code == 404:
                raise Exception("Don't have credential with this id.")
            try:
                error_data = e.response.json()
                if (
                    isinstance(error_data, dict)
                    and error_data.get("success") is False
                    and "don't have credential with this id" in str(error_data.get("data", ""))
                ):
                    raise Exception("Don't have credential with this id.")
            except Exception:
                pass
            raise Exception(f"Error fetching: hmmm?")
        tx_data = tx_resp.json()
        try:
            events_resp = await client.get(f"{BASE_URL}/{credential_id}/events")
            events_resp.raise_for_status()
        except httpx.HTTPError as e:
            raise Exception(f"Error fetching events: {e}")
        events_data = events_resp.json()
    result = {
        "verify": tx_data.get("verify", False),
        "name": tx_data.get("blockcerts_proof", {}).get("credentialSubject", {}).get("name"),
        "certification": tx_data.get("blockcerts_proof", {}).get("credentialSubject", {}).get("claim", {}).get("name"),
        "description": tx_data.get("blockcerts_proof", {}).get("credentialSubject", {}).get("claim", {}).get("description"),
        "issued_on": tx_data.get("blockcerts_proof", {}).get("issuanceDate"),
        "expires_on": tx_data.get("blockcerts_proof", {}).get("expirationDate"),
        "id": tx_data.get("blockcerts_proof", {}).get("id"),
        "blockchain_address": tx_data.get("block_credential_address"),
        "events": events_data.get("events", []),
    }
    return result
