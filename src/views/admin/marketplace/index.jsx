/*!
  _   _  ___  ____  ___ ________  _   _   _   _ ___   
 | | | |/ _ \|  _ \|_ _|__  / _ \| \ | | | | | |_ _| 
 | |_| | | | | |_) || |  / / | | |  \| | | | | || | 
 |  _  | |_| |  _ < | | / /| |_| | |\  | | |_| || |
 |_| |_|\___/|_| \_\___/____\___/|_| \_|  \___/|___|
                                                                                                                                                                                                                                                                                                                                       
=========================================================
* Horizon UI - v1.1.0
=========================================================

* Product Page: https://www.horizon-ui.com/
* Copyright 2023 Horizon UI (https://www.horizon-ui.com/)

* Designed and Coded by Simmmple

=========================================================

* The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

*/

// Chakra imports
import { Box, SimpleGrid } from "@chakra-ui/react";
import DevelopmentTable from "views/admin/dataTables/components/DevelopmentTable";
import CheckTable from "views/admin/dataTables/components/CheckTable";
import ColumnsTable from "views/admin/dataTables/components/ColumnsTable";
import ComplexTable from "views/admin/dataTables/components/ComplexTable";
import IconBox from "components/icons/IconBox";
import SuggestionCard from "./components/SuggestionCard";
import { useState, useEffect } from "react";
import axios from "axios";
import {
  columnsDataDevelopment,
  columnsDataCheck,
  columnsDataColumns,
  columnsDataComplex,
} from "views/admin/dataTables/variables/columnsData";
import tableDataDevelopment from "views/admin/dataTables/variables/tableDataDevelopment.json";
import tableDataCheck from "views/admin/dataTables/variables/tableDataCheck.json";
import tableDataColumns from "views/admin/dataTables/variables/tableDataColumns.json";
import tableDataComplex from "views/admin/dataTables/variables/tableDataComplex.json";
import React from "react";
import { TriangleDownIcon } from "@chakra-ui/icons";
import RnD from "./components/RnD";
import routeCard from "./components/routeCard";

export default function Settings() {

  const [routes, setRoutes] = useState([]);
  const [loading, setLoading] = useState(true);
  useEffect(() => {
     const fetchData = async () => {
      try{
      const response = await axios.get("http://127.0.0.1:8000/api/routes");
      setRoutes(response.data.routes);
      setLoading(false);
      } catch (e) {
        console.log(e);
        setLoading(false);
      }
    };
    fetchData();
  }, []);

  // Chakra Color Mode
  return (
    <Box pt={{ base: "130px", md: "80px", xl: "80px" }}>
      <SimpleGrid
        mb='20px'
        columns={{ sm: 1, md: 1 }}
        spacing={{ base: "20px", xl: "20px" }}>
        {/* <DevelopmentTable
          columnsData={columnsDataDevelopment}
          tableData={tableDataDevelopment}
        /> */}
        <>
        {routes.map((route, index) => (
          <SuggestionCard key={index}
          name={route.name}
          duration={route.duration}
          cost={route.cost}
          carbonEmission={route.carbonEmission}
           />
        ))}
        </>
        {/* <routeCard/> */}
      </SimpleGrid>
    </Box>
  );
}
