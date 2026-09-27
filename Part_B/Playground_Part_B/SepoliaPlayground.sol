// SPDX-License-Identifier: MIT


pragma solidity ^0.8.34;

contract SepoliaPlayground {
    address public owner;
    string public message;
    uint256 public updateCount;
    bool public paused;

    mapping(address => uint256) public deposits;

    event MessageUpdated(
        address indexed updatedBy,
        string previousMessage,
        string newMessage,
        uint256 updateNumber
    );
    event DepositReceived(address indexed sender, uint256 amount);
    event DepositWithdrawn(address indexed recipient, uint256 amount);
    event OwnershipTransferred(
        address indexed previousOwner,
        address indexed newOwner
    );
    event PauseStatusChanged(bool isPaused);

    error EmptyMessage();
    error ZeroDeposit();
    error InsufficientDeposit(uint256 available, uint256 requested);
    error TransferFailed();
    error NotOwner();
    error InvalidOwner();
    error ContractPaused();

    modifier onlyOwner() {
        if (msg.sender != owner) revert NotOwner();
        _;
    }

    modifier whenNotPaused() {
        if (paused) revert ContractPaused();
        _;
    }

    constructor(string memory initialMessage) {
        if (bytes(initialMessage).length == 0) revert EmptyMessage();

        owner = msg.sender;
        message = initialMessage;
    }

    function updateMessage(string calldata newMessage) external whenNotPaused {
        if (bytes(newMessage).length == 0) revert EmptyMessage();

        string memory previousMessage = message;
        message = newMessage;
        updateCount++;

        emit MessageUpdated(
            msg.sender,
            previousMessage,
            newMessage,
            updateCount
        );
    }

    function deposit() external payable whenNotPaused {
        _recordDeposit(msg.sender, msg.value);
    }

    function withdraw(uint256 amount) external {
        uint256 available = deposits[msg.sender];
        if (amount == 0 || amount > available) {
            revert InsufficientDeposit(available, amount);
        }

        deposits[msg.sender] = available - amount;

        (bool success, ) = payable(msg.sender).call{value: amount}("");
        if (!success) revert TransferFailed();

        emit DepositWithdrawn(msg.sender, amount);
    }

    function transferOwnership(address newOwner) external onlyOwner {
        if (newOwner == address(0)) revert InvalidOwner();

        address previousOwner = owner;
        owner = newOwner;

        emit OwnershipTransferred(previousOwner, newOwner);
    }

    function setPaused(bool newStatus) external onlyOwner {
        paused = newStatus;
        emit PauseStatusChanged(newStatus);
    }

    function getContractBalance() external view returns (uint256) {
        return address(this).balance;
    }

    receive() external payable whenNotPaused {
        _recordDeposit(msg.sender, msg.value);
    }

    function _recordDeposit(address sender, uint256 amount) private {
        if (amount == 0) revert ZeroDeposit();

        deposits[sender] += amount;
        emit DepositReceived(sender, amount);
    }
}
