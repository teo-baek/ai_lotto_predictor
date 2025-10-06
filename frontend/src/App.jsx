import React from "react";
import LottoPredictor from "./components/LottoPredictor";

const App = () => {
  return (
    <div style={{ backgroundColor: "#1e1e1e", color: "#fff", minHeight: "100vh", padding: "2rem" }}>
      <h1 style={{ color: "#00BFFF", fontWeight: "bold" }}>🎯 AI Lotto Predictor</h1>
      <LottoPredictor />
    </div>
  );
};

export default App;
