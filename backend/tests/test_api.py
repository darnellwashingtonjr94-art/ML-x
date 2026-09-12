def test_health_check(test_client):
    response = test_client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy", "version": "1.0.0"}

def test_pytorch_inference_route(test_client):
    payload = {
        "data": [[1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]],
        "preprocess": False
    }
    response = test_client.post("/api/v1/predict/pytorch", json=payload)
    assert response.status_code == 200
    
    data = response.json()
    assert data["framework"] == "PyTorch"
    assert "prediction" in data
