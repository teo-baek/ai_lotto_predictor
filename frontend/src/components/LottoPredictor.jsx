import React, { useState } from "react";
import axios from "axios";
import FrequencyChart from "./FrequencyChart";

const LottoPredictor = () => {
  const [results, setResults] = useState([]);
  const [freq, setFreq] = useState({});

  const handlePredict = async () => {
    try {
      const res = await axios.get("http://localhost:8000/api/predict");
      setResults(res.data.predictions);
      setFreq(res.data.frequency);
    } catch (err) {
      console.error(err);
    }
  };

  return (
    <div style={{ marginTop: "1rem" }}>
      <button onClick={handlePredict} style={{ backgroundColor: "#0078D7", color: "white", padding: "0.5rem 1rem", borderRadius: "6px" }}>
        🔢 예측 번호 생성
      </button>

      {results.length > 0 && (
        <div style={{ marginTop: "2rem" }}>
          <h3>📊 예측 결과</h3>
          {results.map((r, i) => (
            <div key={i} style={{ marginBottom: "0.8rem" }}>
              <strong>세트 {i + 1}</strong> — {r.numbers.join(", ")}  
              <br /> 신뢰도: {r.confidence}%
            </div>
          ))}
          <FrequencyChart freq={freq} />
        </div>
      )}
    </div>
  );
};

export default LottoPredictor;
