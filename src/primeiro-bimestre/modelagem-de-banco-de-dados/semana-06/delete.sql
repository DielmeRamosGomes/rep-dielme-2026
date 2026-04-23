create database db_store;
-- Criação da tabela de clientes
CREATE TABLE db_store.Clientes (
    ClienteID INT PRIMARY KEY AUTO_INCREMENT,
    Nome VARCHAR(100),
    Email VARCHAR(100),
    Telefone VARCHAR(15)
);

-- Criação da tabela de pedidos
CREATE TABLE db_store.Pedidos (
    PedidoID INT PRIMARY KEY AUTO_INCREMENT,
    ClienteID INT,
    DataPedido DATE,
    Status VARCHAR(50),
    ValorTotal DECIMAL(10, 2),
    FOREIGN KEY (ClienteID) REFERENCES Clientes(ClienteID)
);
-- Inserir dados na tabela de Clientes
INSERT INTO db_store.Clientes (Nome, Email, Telefone)
VALUES 
('Carlos Silva', 'carlos.silva@email.com', '123456789'),
('Maria Souza', 'maria.souza@email.com', '987654321');

-- Inserir dados na tabela de Pedidos
INSERT INTO db_store.Pedidos (ClienteID, DataPedido, Status, ValorTotal)
VALUES
(1, '2021-12-15', 'Cancelado', 50.00),  -- Pedido antigo e cancelado
(1, '2022-05-20', 'Finalizado', 200.00), -- Pedido finalizado
(2, '2023-03-10', 'Cancelado', 15.00),  -- Pedido cancelado mais recente
(2, '2022-07-25', 'Pendente', 9.50);   -- Pedido com valor baixo

select * from db_store.Clientes;

select * from db_store.Pedidos;





