# Analysis of Alternatives: Raspberry Pi Models

## 1. Introduction

**Problem:** The project requires a low-cost, low-power computing device to run the Python script for the Lithrop Ledger newsletter automatically every day.

**Goal:** To select the most suitable Raspberry Pi model for this task, balancing cost, performance, and ease of use.

This document analyzes three relevant Raspberry Pi models.

---

## 2. Alternatives

### Raspberry Pi Model Comparison

The primary task is to run a Python script that involves API calls, text processing, and sending an email. This is not computationally intensive. The main factors for comparison are price, connectivity (for API calls), and power consumption.

| Feature | Raspberry Pi Zero | Raspberry Pi Zero 2 W | Raspberry Pi 4 Model B |
| :--- | :--- | :--- | :--- |
| **Price** | ~$5 | ~$15 | ~$35+ |
| **CPU** | 1GHz single-core | 1GHz quad-core 64-bit | 1.5GHz quad-core 64-bit |
| **RAM** | 512MB | 512MB | 1GB, 2GB, 4GB, or 8GB |
| **Connectivity** | Requires external adapter | Built-in Wi-Fi & Bluetooth | Built-in Wi-Fi & Bluetooth |
| **Power (Idle)** | ~0.8W | ~1W | ~3.4W |
| **Ease of Setup** | **Medium.** Requires soldering headers and using a USB Wi-Fi adapter. | **Easy.** Headers may need soldering, but Wi-Fi is integrated. | **Easy.** Comes with all ports and connectivity built-in. |
| **Suitability** | **Viable.** The most affordable, but the setup is more involved. | **Recommended.** The best balance of price, performance, and features. | **Overkill.** More powerful and expensive than necessary for this task. |

### In-Depth Analysis

*   **Raspberry Pi Zero:**
    *   **Pros:** Extremely cheap and small.
    *   **Cons:** The lack of built-in networking is a major drawback. It requires purchasing a separate USB OTG adapter and a USB Wi-Fi dongle, which adds to the cost and complexity. The single-core processor is sufficient for this task but offers no headroom.

*   **Raspberry Pi Zero 2 W:**
    *   **Pros:** A significant upgrade over the original Zero for a small price increase. The quad-core processor is more than capable, and the built-in Wi-Fi simplifies the setup immensely. It maintains a very small form factor and low power consumption.
    *   **Cons:** Can be difficult to find in stock due to high demand.

*   **Raspberry Pi 4 Model B:**
    *   **Pros:** A very powerful and versatile single-board computer with ample processing power and RAM for future project expansions. It has a full suite of ports.
    *   **Cons:** The most expensive option and consumes significantly more power. For the sole purpose of running this script, it is excessive.

---

## 3. Recommendation

For the Lithrop Ledger project, the **Raspberry Pi Zero 2 W is the highly recommended choice.**

**Justification:**

1.  **Optimal Balance:** It hits the sweet spot between cost, performance, and convenience. The built-in Wi-Fi is the most critical feature that makes it superior to the original Pi Zero for this internet-reliant project.
2.  **Sufficient Power:** The quad-core CPU provides plenty of power for the current script and any likely future enhancements, such as more complex text processing or handling more data.
3.  **Low Operating Cost:** Its low power consumption makes it ideal for an always-on, 24/7 task.

While the **Raspberry Pi Zero** is a workable alternative for the budget-conscious user who is comfortable with extra hardware setup, the **Raspberry Pi Zero 2 W** provides a much smoother experience for a modest additional cost. The Raspberry Pi 4 is not recommended unless there is a clear, immediate need for its additional power and I/O capabilities.
