def test_get_activities_returns_activity_details(client):
    # Arrange
    expected_activity = "Chess Club"

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    activities = response.json()
    assert expected_activity in activities
    assert set(activities[expected_activity]) == {
        "description",
        "schedule",
        "max_participants",
        "participants",
    }
    assert isinstance(activities[expected_activity]["participants"], list)
