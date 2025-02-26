import { BrowserRouter, Routes, Route } from "react-router-dom";
import Home from "./pages/Home";
import Categories from "./pages/Categories";
import Subscriptions from "./pages/Subscriptions";
import Support from "./pages/Support";
import Modules from "./pages/Modules";
import Resources from "./pages/Resources";
import AdminDashboard from "./pages/AdminDashboard";

import React from "react";

const routes = () => {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/categories" element={<Categories />} />
        <Route path="/subscriptions" element={<Subscriptions />} />
        <Route path="/support" element={<Support />} />
        <Route path="/modules" element={<Modules />} />
        <Route path="/resources" element={<Resources />} />
        <Route path="/admin" element={<AdminDashboard />} />
      </Routes>
    </BrowserRouter>
  );
};

export default routes;
