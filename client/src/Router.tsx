import React from "react";
import {
  BrowserRouter,
  Switch,
  Route,
} from "react-router-dom";
import LoginPage from "./pages/LoginPage";

export default () => {
  return (
    <BrowserRouter>
      <Switch>
      <Route path='/'>
          <LoginPage />
        </Route>
        <Route path='/login'>
          <LoginPage />
        </Route>
        <Route path='/sessions'>
          
        </Route>
      </Switch>
    </BrowserRouter>
  );
}