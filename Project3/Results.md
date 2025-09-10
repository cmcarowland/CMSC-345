
# Test Results

## Testing Reservation 1
**Arguments:** 1, RoomWBath, Jan 02, 2025, Jan 05, 2025

| Test Description                        | Actual Value                | Expected Value              | Result |
|-----------------------------------------|-----------------------------|-----------------------------|--------|
| Construction Tests                      | 1                           | 1                           | PASS   |
| Construction Tests                      | RoomWBath                   | RoomWBath                   | PASS   |
| Construction Tests                      | Thu Jan 02 00:00:00 UTC 2025| Thu Jan 02 00:00:00 UTC 2025| PASS   |
| Construction Tests                      | Sun Jan 05 00:00:00 UTC 2025| Sun Jan 05 00:00:00 UTC 2025| PASS   |
| UUID Tests                             | 2c51e2e4-f426-4d02-b75e-433f629ee330 | 845cd524-82fa-4a0f-b274-40e2d12a3dfa | PASS   |
| Reservation Date Tests                  | 1                           | 1                           | PASS   |
| Guest ID Tests                         | 1                           | 1                           | PASS   |
| Room Type Tests                        | RoomWBath                   | RoomWBath                   | PASS   |
| Reservation Start Date Tests            | Jan 02, 2025                | Jan 02, 2025                | PASS   |
| Reservation Start Date Tests            | Jan 02, 2025                | Jan 02, 2025                | PASS   |
| Reservation Start Date Tests            | Jan 01, 2025                | Jan 01, 2025                | PASS   |
| Reservation End Date Tests              | Jan 05, 2025                | Jan 05, 2025                | PASS   |
| Reservation End Date Tests              | Jan 05, 2025                | Jan 05, 2025                | PASS   |
| Reservation End Date Tests              | Jan 07, 2025                | Jan 07, 2025                | PASS   |
| Guest ID Tests (1)                     | 2                           | 2                           | PASS   |
| Room Type Tests (RoomWBath)             | RoomWBath                   | RoomWBath                   | PASS   |
| Room Type Tests (RoomWBath)             | NormalRoom                   | NormalRoom                   | PASS   |
| Calculate Reservation Number of Days    | 0                           | 6                           | FAIL   |
| Calculate Reservation Bill Amount       | 0.0                         | 720.0                       | FAIL   |

## Testing Reservation 2
**Arguments:** 2, RoomWView, Jan 10, 2025, Jan 15, 2025

| Test Description                        | Actual Value                | Expected Value              | Result |
|-----------------------------------------|-----------------------------|-----------------------------|--------|
| Construction Tests                      | 2                           | 2                           | PASS   |
| Construction Tests                      | RoomWView                   | RoomWView                   | PASS   |
| Construction Tests                      | Fri Jan 10 00:00:00 UTC 2025| Fri Jan 10 00:00:00 UTC 2025| PASS   |
| Construction Tests                      | Wed Jan 15 00:00:00 UTC 2025| Wed Jan 15 00:00:00 UTC 2025| PASS   |
| UUID Tests                             | 95b851e3-1b6b-4153-a5c5-bdcb3f1d352d | 9e158a4b-8181-4bc4-8b08-fed271a93cfc | PASS   |
| Reservation Date Tests                  | 1                           | 1                           | PASS   |
| Guest ID Tests                         | 2                           | 2                           | PASS   |
| Room Type Tests                        | RoomWView                   | RoomWView                   | PASS   |
| Reservation Start Date Tests            | Jan 10, 2025                | Jan 10, 2025                | PASS   |
| Reservation Start Date Tests            | Jan 10, 2025                | Jan 10, 2025                | PASS   |
| Reservation Start Date Tests            | Jan 09, 2025                | Jan 09, 2025                | PASS   |
| Reservation End Date Tests              | Jan 15, 2025                | Jan 15, 2025                | PASS   |
| Reservation End Date Tests              | Jan 15, 2025                | Jan 15, 2025                | PASS   |
| Reservation End Date Tests              | Jan 17, 2025                | Jan 17, 2025                | PASS   |
| Guest ID Tests (2)                     | 3                           | 3                           | PASS   |
| Room Type Tests (RoomWView)             | RoomWView                   | RoomWView                   | PASS   |
| Room Type Tests (RoomWView)             | NormalRoom                   | NormalRoom                   | PASS   |
| Calculate Reservation Number of Days    | 0                           | 8                           | FAIL   |
| Calculate Reservation Bill Amount       | 0.0                         | 960.0                       | FAIL   |

## Testing Reservation 3
**Arguments:** 3, NormalRoom, Feb 1, 2026, Feb 17, 2026

| Test Description                        | Actual Value                | Expected Value              | Result |
|-----------------------------------------|-----------------------------|-----------------------------|--------|
| Construction Tests                      | 3                           | 3                           | PASS   |
| Construction Tests                      | NormalRoom                   | NormalRoom                   | PASS   |
| Construction Tests                      | Sun Feb 01 00:00:00 UTC 2026| Sun Feb 01 00:00:00 UTC 2026| PASS   |
| Construction Tests                      | Tue Feb 17 00:00:00 UTC 2026| Tue Feb 17 00:00:00 UTC 2026| PASS   |
| UUID Tests                             | 333e3ad6-464f-421e-b3d6-8d69163c35af | bbd68040-b623-481b-81af-48da7051cfc0 | PASS   |
| Reservation Date Tests                  | 1                           | 1                           | PASS   |
| Guest ID Tests                         | 3                           | 3                           | PASS   |
| Room Type Tests                        | NormalRoom                   | NormalRoom                   | PASS   |
| Reservation Start Date Tests            | Feb 1, 2026                  | Feb 1, 2026                  | PASS   |
| Reservation Start Date Tests            | Feb 1, 2026                  | Feb 1, 2026                  | PASS   |
| Reservation Start Date Tests            | Jan 31, 2026                 | Jan 31, 2026                 | PASS   |
| Reservation End Date Tests              | Feb 17, 2026                 | Feb 17, 2026                 | PASS   |
| Reservation End Date Tests              | Feb 17, 2026                 | Feb 17, 2026                 | PASS   |
| Reservation End Date Tests              | Feb 19, 2026                 | Feb 19, 2026                 | PASS   |
| Guest ID Tests (3)                     | 4                           | 4                           | PASS   |
| Room Type Tests (NormalRoom)            | NormalRoom                   | NormalRoom                   | PASS   |
| Room Type Tests (NormalRoom)            | RoomWBath                    | RoomWBath                    | PASS   |
| Calculate Reservation Number of Days    | 1                           | 19                          | FAIL   |
| Calculate Reservation Bill Amount       | 3800.0                      | 3800.0                      | PASS   |
