```mermaid

flowchart TD

    node_developer(("Developer"))
    node_sepolia{{"Ethereum Sepolia"}}

    subgraph group_blockchain["Blockchain and proof-of-work"]
        direction TB

        node_chain_app["Blockchain simulation<br/>task_1_blockchain.py"]
        node_block_hashing["SHA-256 block hashing"]
        node_chain_integrity["Integrity and tamper detection"]

        node_pow_app["Proof-of-work simulation<br/>task_2_proof_of_work.py"]
        node_nonce_search["Nonce-based mining"]
        node_pow_metrics["Difficulty and performance metrics"]
        node_pow_files["CSV result exports"]
    end

    subgraph group_crypto["Cryptography"]
        direction TB

        node_ecdsa_app["ECDSA implementation<br/>task_3_ecdsa.py"]
        node_key_generation["SECP256K1 key generation"]
        node_key_compression["Public key compression"]
        node_key_files["Private and public key export"]
        node_signature_verification["Digital signature verification"]
    end

    subgraph group_ethereum["Ethereum smart contracts"]
        direction TB

        node_aut_contract["AUT assessment contract<br/>Storage.sol"]
        node_storage_operations["On-chain data storage and retrieval"]

        node_playground_contract["Sepolia interaction playground<br/>SepoliaPlayground.sol"]
        node_state_updates["State updates and event logs"]
        node_eth_operations["Test ETH deposits and withdrawals"]
        node_access_control["Ownership and pause controls"]
    end

    node_developer -->|"runs"| node_chain_app
    node_chain_app -->|"creates and hashes blocks"| node_block_hashing
    node_chain_app -->|"validates blockchain integrity"| node_chain_integrity
    node_block_hashing -->|"supports validation"| node_chain_integrity

    node_developer -->|"runs"| node_pow_app
    node_pow_app -->|"searches for a valid nonce"| node_nonce_search
    node_nonce_search -->|"produces measurements"| node_pow_metrics
    node_pow_app -->|"exports results"| node_pow_files

    node_developer -->|"runs"| node_ecdsa_app
    node_ecdsa_app -->|"generates key pair"| node_key_generation
    node_ecdsa_app -->|"compresses public key"| node_key_compression
    node_ecdsa_app -->|"exports hexadecimal keys"| node_key_files
    node_ecdsa_app -->|"signs and verifies data"| node_signature_verification

    node_developer -->|"compiles and deploys"| node_aut_contract
    node_aut_contract -->|"stores and retrieves values"| node_storage_operations
    node_aut_contract -.->|"deployed to"| node_sepolia

    node_developer -->|"deploys and interacts"| node_playground_contract
    node_playground_contract -->|"changes contract state"| node_state_updates
    node_playground_contract -->|"handles test ETH"| node_eth_operations
    node_playground_contract -->|"restricts administrative actions"| node_access_control
    node_playground_contract -.->|"deployed to"| node_sepolia

    click node_chain_app "https://github.com/panamilit/COMP726-Individual-Technical-Assessment/blob/main/Part_A/task_1_blockchain.py" "Open blockchain simulation" _blank
    click node_pow_app "https://github.com/panamilit/COMP726-Individual-Technical-Assessment/blob/main/Part_A/task_2_proof_of_work.py" "Open proof-of-work simulation" _blank
    click node_ecdsa_app "https://github.com/panamilit/COMP726-Individual-Technical-Assessment/blob/main/Part_A/task_3_ecdsa.py" "Open ECDSA implementation" _blank
    click node_aut_contract "https://github.com/panamilit/COMP726-Individual-Technical-Assessment/blob/main/Part_B/AUT_Part_B/Storage.sol" "Open assessment contract" _blank
    click node_playground_contract "https://github.com/panamilit/COMP726-Individual-Technical-Assessment/blob/main/Part_B/Playground_Part_B/SepoliaPlayground.sol" "Open Sepolia playground" _blank

    classDef blockchain fill:#dbeafe,stroke:#2563eb,stroke-width:1.5px,color:#172554
    classDef cryptography fill:#fef3c7,stroke:#d97706,stroke-width:1.5px,color:#78350f
    classDef ethereum fill:#dcfce7,stroke:#16a34a,stroke-width:1.5px,color:#14532d
    classDef external fill:#e0e7ff,stroke:#4f46e5,stroke-width:1.5px,color:#312e81

    class node_chain_app,node_block_hashing,node_chain_integrity,node_pow_app,node_nonce_search,node_pow_metrics,node_pow_files blockchain
    class node_ecdsa_app,node_key_generation,node_key_compression,node_key_files,node_signature_verification cryptography
    class node_aut_contract,node_storage_operations,node_playground_contract,node_state_updates,node_eth_operations,node_access_control ethereum
    class node_developer,node_sepolia external

    ```