// SPDX-License-Identifier: MIT


pragma solidity ^0.8.34;

contract Storage {
    uint private number;
    string public courseCode;

    function store(uint newNumber) public {
        number = newNumber;
    }

    function retrieve() public view returns (uint) {
        return number;
    }

    function setCourseCode(string calldata newCourseCode) public {
        courseCode = newCourseCode;
    }
}

