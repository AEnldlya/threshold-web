# Stripe Payments

**Collect $2,500 website payments and manage recurring $100/month maintenance billing**

## What It Does

Use Stripe CLI to:
- Generate payment links for completed websites
- Create invoices for clients
- Set up recurring billing ($100/month maintenance)
- Track payment status
- Issue refunds if needed
- Monitor failed payments

## Setup

1. Get Stripe API keys from: https://dashboard.stripe.com/apikeys
2. Store keys as environment variables:
   ```bash
   export STRIPE_API_KEY="sk_live_..."
   export STRIPE_PUBLISHABLE_KEY="pk_live_..."
   ```
3. Install Stripe CLI: `brew install stripe/stripe-cli/stripe`
4. Authenticate: `stripe login`

## Create Payment Link ($2,500 Website)

```bash
stripe payment_links create \
  --line-items '[{"price_data": {"currency": "usd", "product_data": {"name": "Professional Website"}, "unit_amount": 250000}, "quantity": 1}]'
```

Returns a payment link like: `https://buy.stripe.com/...`

Send this to client: "Your website is ready! Complete payment here: [link]"

## Create Invoice ($100/month Maintenance)

```bash
stripe invoices create \
  --customer cus_xxxxx \
  --collection_method send_invoice \
  --days_until_due 30 \
  --auto_advance false
```

## Set Up Recurring Billing

```bash
stripe subscriptions create \
  --customer cus_xxxxx \
  --items '[{"price": "price_monthly_maintenance"}]'
```

## View Payment Status

```bash
stripe charges list --limit 10
stripe payment_intents list --limit 10
```

## Integration Points

- **With Email**: Send payment link via email when website is ready
- **With Airtable**: Log payment status to "Clients" table
- **With Telegram**: Alert when payment is received

## Commands in OpenClaw

```
/stripe create-payment-link $2500 "Professional Website"
/stripe create-invoice [client-id]
/stripe check-payment [payment-id]
/stripe refund [charge-id]
```

## Testing (Sandbox)

Use test card: `4242 4242 4242 4242`
Expiry: Any future date
CVC: Any 3 digits

## Useful Links

- Stripe Dashboard: https://dashboard.stripe.com
- API Documentation: https://stripe.com/docs
- Payment Links: https://stripe.com/docs/payment-links
- Pricing: $2.9% + $0.30 per transaction (already built into $2,500 price)
