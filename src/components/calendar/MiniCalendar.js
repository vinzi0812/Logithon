import React, { useState } from "react";
import Calendar from "react-calendar";
import "react-calendar/dist/Calendar.css";
import "assets/css/MiniCalendar.css";
import { Text, Icon } from "@chakra-ui/react";
// Chakra imports
import { MdChevronLeft, MdChevronRight } from "react-icons/md";
// Custom components
import Card from "components/card/Card.js";

export default function MiniCalendar(props) {
  const { selectRange, ...rest } = props;
  const [value, onChange] = useState(new Date());
  return (
    <Card
      align='center'
      direction='column'
      w='100%'
      // maxW='max-content'
      p='20px 50px'
      h='max-content'
      {...rest}>
      <Calendar
        onChange={onChange}
        value={value}
        selectRange={selectRange}
        view={"month"}
        tileContent={<Text color='brand.500'></Text>}
        prevLabel={<Icon as={MdChevronLeft} w='30px' h='24px' mt='10px' />}
        nextLabel={<Icon as={MdChevronRight} w='30px' h='24px' mt='10px' />}
      />
    </Card>
  );
}
