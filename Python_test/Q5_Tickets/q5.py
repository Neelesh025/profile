def calculate_ticket_price(seats, timing, is_weekend):
    
    prices = {
        "VIP": 500,
        "REGULAR": 300,
        "ECONOMY": 150
    }
    
    timing_mult = {
        "morning": 0.8,
        "afternoon": 1,
        "evening": 1.2,
        "night": 1.5
    }
    
    base_total = 0
    valid_seats = 0
    
    for seat in seats:
        if seat in prices:
            base_total += prices[seat]
            valid_seats += 1
    
    if valid_seats == 0:
        return "No valid booking"
    
    timing_total = base_total * timing_mult[timing]
    
    if is_weekend:
        timing_total += timing_total * 0.10
    
    discount = 0
    if valid_seats >= 5:
        discount = timing_total * 0.15
        timing_total -= discount
    
    fee = valid_seats * 50
    total_after_fee = timing_total + fee
    
    tax = total_after_fee * 0.12
    
    final_amount = total_after_fee + tax
    
    return {
        "base_total": round(base_total),
        "timing_adjustment": round(timing_total),
        "discount": round(discount),
        "tax": round(tax),
        "final_amount": round(final_amount)
    }


# Example test
result = calculate_ticket_price(
    ["VIP", "REGULAR", "VIP"],
    "evening",
    True
)

print(result)
