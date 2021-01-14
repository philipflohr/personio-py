import json

json_string_absence_alan = """
{
  "success": true,
  "data": [{
      "type": "TimeOffPeriod",
      "attributes": {
        "id": 17205942,
        "status": "approved",
        "comment": "marathon starts at noon",
        "start_date": "1944-09-01T00:00:00+02:00",
        "end_date": "1944-09-01T00:00:00+02:00",
        "days_count": 0.5,
        "half_day_start": 0,
        "half_day_end": 1,
        "time_off_type": {
          "type": "TimeOffType",
          "attributes": {
            "id": 195824,
            "name": "vacation"
          }
        },
        "employee": {
          "type": "Employee",
          "attributes": {
            "id": {
              "label": "ID",
              "value": 2116365
            },
            "first_name": {
              "label": "First name",
              "value": "Alan"
            },
            "last_name": {
              "label": "Last name",
              "value": "Turing"
            },
            "email": {
              "label": "Email",
              "value": "alan@example.org"
            }
          }
        },
        "created_by": "Alan Turing",
        "certificate": {
          "status": "not-required"
        },
        "created_at": "2020-08-21T18:07:06+02:00"
      }
    }, {
      "type": "TimeOffPeriod",
      "attributes": {
        "id": 17205932,
        "status": "approved",
        "comment": "don't you just hate mondays sometimes?",
        "start_date": "1944-07-03T00:00:00+02:00",
        "end_date": "1944-07-03T00:00:00+02:00",
        "days_count": 1,
        "half_day_start": 0,
        "half_day_end": 0,
        "time_off_type": {
          "type": "TimeOffType",
          "attributes": {
            "id": 195824,
            "name": "vacation"
          }
        },
        "employee": {
          "type": "Employee",
          "attributes": {
            "id": {
              "label": "ID",
              "value": 2116365
            },
            "first_name": {
              "label": "First name",
              "value": "Alan"
            },
            "last_name": {
              "label": "Last name",
              "value": "Turing"
            },
            "email": {
              "label": "Email",
              "value": "alan@example.org"
            }
          }
        },
        "created_by": "Alan Turing",
        "certificate": {
          "status": "not-required"
        },
        "created_at": "2020-08-21T18:06:02+02:00"
      }
    }, {
      "type": "TimeOffPeriod",
      "attributes": {
        "id": 17205920,
        "status": "approved",
        "comment": "summer vacation",
        "start_date": "1944-08-07T00:00:00+02:00",
        "end_date": "1944-08-20T00:00:00+02:00",
        "days_count": 10,
        "half_day_start": 0,
        "half_day_end": 0,
        "time_off_type": {
          "type": "TimeOffType",
          "attributes": {
            "id": 195824,
            "name": "vacation"
          }
        },
        "employee": {
          "type": "Employee",
          "attributes": {
            "id": {
              "label": "ID",
              "value": 2116365
            },
            "first_name": {
              "label": "First name",
              "value": "Alan"
            },
            "last_name": {
              "label": "Last name",
              "value": "Turing"
            },
            "email": {
              "label": "Email",
              "value": "alan@example.org"
            }
          }
        },
        "created_by": "Alan Turing",
        "certificate": {
          "status": "not-required"
        },
        "created_at": "2020-08-21T18:05:04+02:00"
      }
    }
  ]
}
"""
json_dict_absence_alan = json.loads(json_string_absence_alan)


json_string_absence_types = """
{
  "success": true,
  "data": [{
      "type": "TimeOffType",
      "attributes": {
        "id": 195824,
        "name": "vacation"
      }
    }, {
      "type": "TimeOffType",
      "attributes": {
        "id": 195825,
        "name": "paid leave"
      }
    }, {
      "type": "TimeOffType",
      "attributes": {
        "id": 195826,
        "name": "sick"
      }
    }
  ]
}
"""
json_dict_absence_types = json.loads(json_string_absence_types)
