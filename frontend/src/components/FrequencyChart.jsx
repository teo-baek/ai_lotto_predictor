import React from "react";
import { BarChart, Bar, XAxis, YAxis, Tooltip, CartesianGrid, ResponsiveContainer } from "recharts";

const FrequencyChart = ({ freq }) => {
  const data = Object.entries(freq).map(([num, count]) => ({
    number: parseInt(num),
    count,
  }));

  return (
    <div style={{ marginTop: "2rem" }}>
      <h4>🎯 예측 번호 분포</h4>
      <ResponsiveContainer width="100%" height={300}>
        <BarChart data={data}>
          <CartesianGrid strokeDasharray="3 3" stroke="#555" />
          <XAxis dataKey="number" stroke="#ccc" />
          <YAxis stroke="#ccc" />
          <Tooltip />
          <Bar dataKey="count" fill="#00BFFF" />
        </BarChart>
      </ResponsiveContainer>
    </div>
  );
};

export default FrequencyChart;
