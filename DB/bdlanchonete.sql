-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Tempo de geração: 24-Set-2020 às 04:04
-- Versão do servidor: 10.4.14-MariaDB
-- versão do PHP: 7.2.33

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `bdlanchonete`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `clientes`
--

CREATE TABLE `clientes` (
  `cod_cliente` int(11) NOT NULL,
  `nome_cliente` varchar(255) DEFAULT NULL,
  `datanasc_cliente` date NOT NULL,
  `cpf_cliente` varchar(11) NOT NULL,
  `rg_cliente` varchar(9) NOT NULL,
  `end_cliente` varchar(255) NOT NULL,
  `nunend_cliente` varchar(50) NOT NULL,
  `bairro_cliente` varchar(255) NOT NULL,
  `cep_cliente` varchar(8) NOT NULL,
  `cidade_cliente` varchar(255) NOT NULL,
  `uf_cliente` varchar(2) NOT NULL,
  `fone_cliente` varchar(12) NOT NULL,
  `celular_cliente` varchar(12) NOT NULL,
  `email_cliente` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Extraindo dados da tabela `clientes`
--

INSERT INTO `clientes` (`cod_cliente`, `nome_cliente`, `datanasc_cliente`, `cpf_cliente`, `rg_cliente`, `end_cliente`, `nunend_cliente`, `bairro_cliente`, `cep_cliente`, `cidade_cliente`, `uf_cliente`, `fone_cliente`, `celular_cliente`, `email_cliente`) VALUES
(0, 'teste', '1991-01-01', '', '', '', '', '', '', '', '', '', '', ''),
(1, 'itamar Nascimento', '1992-11-01', '08919673462', '7996030', 'rua tal', '237', 'fragoso', '52130360', 'olinda', 'PE', '', '81985278547', 'itamarasa@gmail.com'),
(2, 'debora', '0000-00-00', '', '', '', '', '', '', '', 'PE', '', '', ''),
(6, 'neto', '0000-00-00', '', '', '', '', '', '', '', '', '', '', ''),
(7, 'merabe', '0000-00-00', '', '', '', '', '', '', '', '', '', '', ''),
(8, '', '0000-00-00', '', '', '', '', '', '', '', '', '', '', ''),
(9, '', '2020-10-01', '', '', '', '', '', '', '', '', '', '', '');

-- --------------------------------------------------------

--
-- Estrutura da tabela `itens_venda`
--

CREATE TABLE `itens_venda` (
  `id_venda` int(11) NOT NULL,
  `cod_prod_venda` int(11) NOT NULL,
  `prod_des_venda` varchar(255) NOT NULL,
  `un_venda` varchar(3) NOT NULL,
  `qtd_venda` int(11) NOT NULL,
  `vl_init_venda` float NOT NULL,
  `vl_total_venda` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Extraindo dados da tabela `itens_venda`
--

INSERT INTO `itens_venda` (`id_venda`, `cod_prod_venda`, `prod_des_venda`, `un_venda`, `qtd_venda`, `vl_init_venda`, `vl_total_venda`) VALUES
(6, 4, 'Coxinha', 'UN', 1, 4.5, 4.5),
(8, 4, 'Coxinha', 'UN', 1, 4.5, 4.5),
(8, 5, '1', 'UN', 1, 1, 1),
(8, 4, 'Coxinha', 'UN', 10, 4.5, 45),
(9, 4, 'Coxinha', 'UN', 1, 4.5, 4.5),
(10, 4, 'Coxinha', 'UN', 1, 4.5, 4.5),
(11, 4, 'Coxinha', 'UN', 1, 4.5, 4.5),
(11, 5, '1', 'IN', 1, 1, 1),
(12, 4, 'Coxinha', 'UN', 1, 4.5, 4.5),
(13, 4, 'Coxinha', 'UN', 1, 4.5, 4.5),
(14, 4, 'Coxinha', 'UN', 1, 4.5, 4.5),
(15, 4, 'Coxinha', 'UN', 1, 4.5, 4.5),
(15, 5, '1', 'UN', 1, 1, 1),
(15, 4, 'Coxinha', 'UN', 1, 4.5, 4.5),
(15, 4, 'Coxinha', 'UN', 1, 4.5, 4.5),
(16, 4, 'Coxinha', 'UN', 1, 4.5, 4.5),
(16, 5, '1', 'UN', 1, 1, 1),
(16, 4, 'Coxinha', 'UN', 1, 4.5, 4.5),
(16, 6, 'te', 'UN', 1, 10, 10),
(17, 4, 'Coxinha', 'UN', 1, 4.5, 4.5),
(17, 4, 'Coxinha', 'UN', 1, 4.5, 4.5),
(17, 6, 'te', 'UN', 1, 10, 10),
(18, 4, 'Coxinha', 'un', 1, 4.5, 4.5),
(18, 4, 'Coxinha', 'un', 1, 4.5, 4.5),
(19, 4, 'Coxinha', 'UN', 1, 4.5, 4.5),
(20, 4, 'Coxinha', 'UN', 1, 4.5, 4.5),
(20, 5, '1', 'UN', 1, 1, 1),
(21, 4, 'Coxinha', 'UN', 1, 4.5, 4.5),
(22, 4, 'Coxinha', 'UN', 1, 4.5, 4.5),
(22, 6, 'te', 'UN', 1, 10, 10),
(23, 4, 'Coxinha', 'UN', 1, 4.5, 4.5),
(24, 4, 'Coxinha', 'UN', 1, 4.5, 4.5),
(25, 4, 'Coxinha', 'UN', 1, 4.5, 4.5),
(25, 6, 'te', 'UN', 1, 10, 10),
(26, 4, 'Coxinha', 'UN', 1, 4.5, 4.5),
(26, 6, 'te', 'UN', 1, 10, 10),
(33, 4, 'Coxinha', 'UN', 1, 4.5, 4.5),
(34, 4, 'Coxinha', 'UN', 1, 4.5, 4.5),
(35, 4, 'Coxinha', 'UN', 1, 4.5, 4.5),
(35, 4, 'Coxinha', 'UN', 1, 4.5, 4.5),
(36, 4, 'Coxinha', 'UN', 1, 4.5, 4.5),
(37, 4, 'Coxinha', 'UN', 1, 4.5, 4.5),
(38, 4, 'Coxinha', 'UN', 1, 4.5, 4.5),
(39, 4, 'Coxinha', 'UN', 1, 4.5, 4.5),
(40, 4, 'Coxinha', 'UN', 1, 4.5, 4.5),
(41, 4, 'Coxinha', 'UN', 1, 4.5, 4.5),
(42, 4, 'Coxinha', 'UN', 1, 4.5, 4.5),
(44, 4, 'Coxinha', 'UN', 1, 4.5, 4.5),
(46, 4, 'Coxinha', 'UN', 1, 4.5, 4.5),
(48, 4, 'Coxinha', 'UN', 1, 4.5, 4.5);

-- --------------------------------------------------------

--
-- Estrutura da tabela `produtos`
--

CREATE TABLE `produtos` (
  `cod_produto` int(15) NOT NULL,
  `ean_produto` int(30) DEFAULT NULL,
  `nome_produto` varchar(100) NOT NULL,
  `categoria_produto` varchar(100) NOT NULL,
  `descricão_produto` varchar(255) DEFAULT NULL,
  `pre_venda_produto` float(4,2) DEFAULT NULL,
  `pre_custo_produto` float(4,2) DEFAULT NULL,
  `estoque` varchar(5) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Extraindo dados da tabela `produtos`
--

INSERT INTO `produtos` (`cod_produto`, `ean_produto`, `nome_produto`, `categoria_produto`, `descricão_produto`, `pre_venda_produto`, `pre_custo_produto`, `estoque`) VALUES
(4, 12345, 'Coxinha', 'Salgados', 'ok\n', 4.50, 1.00, '87'),
(5, 1, '1', 'Salgados', '1\n', 1.00, 1.00, '-1'),
(6, 12, 'te', 'Doces', '10\n', 10.00, 10.00, '99'),
(7, 332, '', 'Selecione', '\n', 0.00, 0.00, ''),
(8, 1212, '', 'Selecione', '\n', 0.00, 0.00, ''),
(10, 3232, '', 'Selecione', '\n', 0.00, 0.00, ''),
(11, 12121, '', 'Selecione', '\n', 0.00, 0.00, ''),
(12, 15454, '', 'Selecione', '\n', 0.00, 0.00, ''),
(13, 12311, '', 'Selecione', '\n', 0.00, 0.00, ''),
(14, 33565, '', 'Selecione', '\n', 0.00, 0.00, ''),
(15, 4554545, '', 'Selecione', '\n', 0.00, 0.00, ''),
(16, 5555, '', 'Salgados', '\n', 0.00, 0.00, ''),
(17, 3333, '', 'Bebidas', '\n', 1.00, 2.00, ''),
(18, 6666, 'TESEW', 'Selecione', '\n', 2.00, 3.00, ''),
(19, 66, 'TESTE1', 'Salgados', '\n', 2.00, 3.00, '');

-- --------------------------------------------------------

--
-- Estrutura da tabela `tipo_pag`
--

CREATE TABLE `tipo_pag` (
  `cod_pag` int(11) NOT NULL,
  `desc_pag` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Extraindo dados da tabela `tipo_pag`
--

INSERT INTO `tipo_pag` (`cod_pag`, `desc_pag`) VALUES
(1, 'DINHEIRO'),
(2, 'VISA CREDITO'),
(3, 'VISA DEBITO');

-- --------------------------------------------------------

--
-- Estrutura da tabela `usuarios`
--

CREATE TABLE `usuarios` (
  `id` int(4) NOT NULL,
  `nome` varchar(100) NOT NULL,
  `cpf` varchar(11) NOT NULL,
  `senha` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Extraindo dados da tabela `usuarios`
--

INSERT INTO `usuarios` (`id`, `nome`, `cpf`, `senha`) VALUES
(1000, 'itamar', '8919673462', '1'),
(1003, 'debora', '89', '123');

-- --------------------------------------------------------

--
-- Estrutura da tabela `vendas`
--

CREATE TABLE `vendas` (
  `cod_pedido` int(11) NOT NULL,
  `cod_operador` int(11) DEFAULT NULL,
  `id_clientes` int(11) DEFAULT NULL,
  `vl_total` float NOT NULL,
  `pedido_fechado` varchar(1) NOT NULL,
  `data_create` datetime DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Extraindo dados da tabela `vendas`
--

INSERT INTO `vendas` (`cod_pedido`, `cod_operador`, `id_clientes`, `vl_total`, `pedido_fechado`, `data_create`) VALUES
(1, 0, 0, 0, '', '2020-09-12 12:25:11'),
(2, 0, 0, 4.5, '', '2020-09-12 12:29:01'),
(3, 0, 0, 9, '', '2020-09-12 12:35:40'),
(4, 0, 0, 4.5, '', '2020-09-12 12:37:00'),
(5, 0, 0, 4.5, '', '2020-09-12 12:56:33'),
(6, 0, 0, 4.5, '', '2020-09-12 12:58:30'),
(7, 0, 0, 10, '', '2020-09-12 13:02:06'),
(8, 0, 0, 50.5, '', '2020-09-12 13:20:45'),
(9, 0, 0, 5.5, '', '2020-09-12 13:26:31'),
(10, 0, 0, 5.5, '', '2020-09-12 13:28:06'),
(11, 0, 0, 5.5, '', '2020-09-12 13:31:15'),
(12, 0, 0, 4.5, 'S', '2020-09-14 18:20:39'),
(13, 0, 0, 4.5, 'N', '2020-09-14 18:34:32'),
(14, 0, 0, 4.5, 'N', '2020-09-14 19:11:53'),
(15, 0, 0, 14.5, 'S', '2020-09-14 21:07:13'),
(16, 0, 0, 20, 'S', '2020-09-14 21:08:39'),
(17, 0, 0, 19, 'S', '2020-09-14 21:12:09'),
(18, 0, 0, 9, 'S', '2020-09-15 17:58:26'),
(19, 0, 0, 4.5, 'S', '2020-09-19 11:55:37'),
(20, 0, 0, 5.5, 'N', '2020-09-19 11:57:07'),
(21, 0, 0, 14.5, 'N', '2020-09-19 12:02:19'),
(22, 0, 0, 14.5, 'N', '2020-09-19 12:05:37'),
(23, 0, 0, 14.5, 'N', '2020-09-19 12:38:02'),
(24, 0, 0, 14.5, 'N', '2020-09-19 12:40:20'),
(25, 0, 0, 14.5, 'N', '2020-09-19 12:44:54'),
(26, 0, 0, 14.5, 'N', '2020-09-19 12:47:53'),
(27, 0, 0, 0, 'N', '2020-09-23 22:07:12'),
(28, 0, 0, 0, 'N', '2020-09-23 22:07:16'),
(29, 0, 0, 0, 'N', '2020-09-23 22:07:20'),
(30, 0, 0, 0, 'N', '2020-09-23 22:07:20'),
(31, 0, 0, 0, 'N', '2020-09-23 22:07:20'),
(32, 0, 0, 0, 'N', '2020-09-23 22:07:21'),
(33, 0, 0, 4.5, 'N', '2020-09-23 22:07:31'),
(34, 0, 0, 4.5, 'N', '2020-09-23 22:12:16'),
(35, 0, 0, 9, 'N', '2020-09-23 22:13:25'),
(36, 0, 0, 4.5, 'N', '2020-09-23 22:15:46'),
(37, 0, 0, 4.5, 'N', '2020-09-23 22:16:11'),
(38, 0, 0, 4.5, 'N', '2020-09-23 22:41:21'),
(39, 0, 0, 4.5, 'N', '2020-09-23 22:42:14'),
(40, 0, 0, 4.5, 'N', '2020-09-23 22:45:09'),
(41, 0, 0, 4.5, 'N', '2020-09-23 22:45:30'),
(42, 0, 0, 4.5, 'S', '2020-09-23 22:52:11'),
(43, 0, 0, 0, 'N', '2020-09-23 22:52:18'),
(44, 0, 0, 4.5, 'S', '2020-09-23 22:53:38'),
(45, 0, 0, 0, 'N', '2020-09-23 22:53:46'),
(46, 0, 0, 4.5, 'S', '2020-09-23 22:57:40'),
(47, 0, 0, 0, 'N', '2020-09-23 22:58:27'),
(48, 0, 0, 4.5, 'S', '2020-09-23 23:02:43');

-- --------------------------------------------------------

--
-- Estrutura da tabela `venda_pag`
--

CREATE TABLE `venda_pag` (
  `id_venda` int(11) NOT NULL,
  `desc_pag` varchar(255) NOT NULL,
  `valor_pag` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Extraindo dados da tabela `venda_pag`
--

INSERT INTO `venda_pag` (`id_venda`, `desc_pag`, `valor_pag`) VALUES
(38, '{VISA CREDITO}', 4.5),
(39, 'DINHEIRO', 4),
(39, '{VISA CREDITO}', 0.5),
(40, 'DINHEIRO', 4.5),
(41, 'Selecione', 4.5),
(42, 'DINHEIRO', 4.5),
(43, 'DINHEIRO', 4.5),
(44, '{VISA CREDITO}', 4.5),
(45, '{VISA CREDITO}', 4.5),
(46, 'DINHEIRO', 4.5),
(47, 'DINHEIRO', 4.5),
(48, 'Selecione', 4.5);

--
-- Índices para tabelas despejadas
--

--
-- Índices para tabela `clientes`
--
ALTER TABLE `clientes`
  ADD PRIMARY KEY (`cod_cliente`);

--
-- Índices para tabela `itens_venda`
--
ALTER TABLE `itens_venda`
  ADD KEY `id_venda` (`id_venda`);

--
-- Índices para tabela `produtos`
--
ALTER TABLE `produtos`
  ADD PRIMARY KEY (`cod_produto`);

--
-- Índices para tabela `tipo_pag`
--
ALTER TABLE `tipo_pag`
  ADD PRIMARY KEY (`cod_pag`);

--
-- Índices para tabela `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`id`);

--
-- Índices para tabela `vendas`
--
ALTER TABLE `vendas`
  ADD PRIMARY KEY (`cod_pedido`);

--
-- Índices para tabela `venda_pag`
--
ALTER TABLE `venda_pag`
  ADD KEY `venda_pag_ibfk_1` (`id_venda`);

--
-- AUTO_INCREMENT de tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `produtos`
--
ALTER TABLE `produtos`
  MODIFY `cod_produto` int(15) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;

--
-- AUTO_INCREMENT de tabela `tipo_pag`
--
ALTER TABLE `tipo_pag`
  MODIFY `cod_pag` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de tabela `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `id` int(4) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1004;

--
-- Restrições para despejos de tabelas
--

--
-- Limitadores para a tabela `itens_venda`
--
ALTER TABLE `itens_venda`
  ADD CONSTRAINT `itens_venda_ibfk_1` FOREIGN KEY (`id_venda`) REFERENCES `vendas` (`cod_pedido`);

--
-- Limitadores para a tabela `venda_pag`
--
ALTER TABLE `venda_pag`
  ADD CONSTRAINT `venda_pag_ibfk_1` FOREIGN KEY (`id_venda`) REFERENCES `vendas` (`cod_pedido`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
