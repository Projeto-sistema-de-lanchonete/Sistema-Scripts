-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Tempo de geração: 18-Nov-2020 às 04:38
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
-- Estrutura da tabela `empresa`
--

CREATE TABLE `empresa` (
  `cod_empresa` int(11) NOT NULL,
  `razao_social` varchar(255) NOT NULL,
  `nome_fantasia` varchar(255) NOT NULL,
  `cpf_cnpj` varchar(11) NOT NULL,
  `ie_empresa` varchar(9) NOT NULL,
  `end_empresa` varchar(255) NOT NULL,
  `nunend_empresa` varchar(50) NOT NULL,
  `bairro_empresa` varchar(255) NOT NULL,
  `cep_empresa` varchar(8) NOT NULL,
  `cidade_empresa` varchar(255) NOT NULL,
  `uf_empresa` varchar(2) NOT NULL,
  `fone_empresa` varchar(12) NOT NULL,
  `email_empresa` varchar(100) NOT NULL,
  `data_create` datetime NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Extraindo dados da tabela `empresa`
--

INSERT INTO `empresa` (`cod_empresa`, `razao_social`, `nome_fantasia`, `cpf_cnpj`, `ie_empresa`, `end_empresa`, `nunend_empresa`, `bairro_empresa`, `cep_empresa`, `cidade_empresa`, `uf_empresa`, `fone_empresa`, `email_empresa`, `data_create`) VALUES
(1, 'Itamar Nascimento', 'Teste', '089196734', '0000', 'Rua tal', '237', 'Agua Fri', '52130360', 'Refice', 'PE', '', 'itamarasa@gmail.com', '2020-10-09 23:42:30');

-- --------------------------------------------------------

--
-- Estrutura da tabela `entradanotas`
--

CREATE TABLE `entradanotas` (
  `cod_entrada` int(11) NOT NULL,
  `nome_operador` varchar(255) DEFAULT NULL,
  `id_fornecedor` int(11) NOT NULL,
  `vl_total` float NOT NULL,
  `nota_fechado` varchar(1) NOT NULL,
  `data_create` datetime DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Extraindo dados da tabela `entradanotas`
--

INSERT INTO `entradanotas` (`cod_entrada`, `nome_operador`, `id_fornecedor`, `vl_total`, `nota_fechado`, `data_create`) VALUES
(1, 'itamar', 1, 5, 'S', '2020-11-18 00:19:02'),
(2, 'itamar', 2, 10, 'S', '2020-11-17 23:48:24'),
(3, 'itamar', 1, 51, 'S', '2020-11-18 00:22:39'),
(4, 'itamar', 1, 5, 'S', '2020-11-18 00:25:52'),
(5, 'itamar', 1, 6, 'S', '2020-11-18 00:27:06'),
(6, 'itamar', 1, 6, 'S', '2020-11-18 00:31:39'),
(7, 'itamar', 1, 6, 'S', '2020-11-18 00:34:04');

-- --------------------------------------------------------

--
-- Estrutura da tabela `fornecedor`
--

CREATE TABLE `fornecedor` (
  `cod_fornecedor` int(11) NOT NULL,
  `razao_social` varchar(255) NOT NULL,
  `nome_fantasia` varchar(255) NOT NULL,
  `cpf_cnpj` varchar(11) NOT NULL,
  `ie_fornecedor` varchar(9) NOT NULL,
  `end_fornecedor` varchar(255) NOT NULL,
  `nunend_fornecedor` varchar(50) NOT NULL,
  `bairro_fornecedor` varchar(255) NOT NULL,
  `cep_fornecedor` varchar(8) NOT NULL,
  `cidade_fornecedor` varchar(255) NOT NULL,
  `uf_fornecedor` varchar(2) NOT NULL,
  `fone_fornecedor` varchar(12) NOT NULL,
  `email_fornecedor` varchar(100) NOT NULL,
  `data_create` datetime NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Extraindo dados da tabela `fornecedor`
--

INSERT INTO `fornecedor` (`cod_fornecedor`, `razao_social`, `nome_fantasia`, `cpf_cnpj`, `ie_fornecedor`, `end_fornecedor`, `nunend_fornecedor`, `bairro_fornecedor`, `cep_fornecedor`, `cidade_fornecedor`, `uf_fornecedor`, `fone_fornecedor`, `email_fornecedor`, `data_create`) VALUES
(1, 'teste 1', '', '', '', '', '', '', '', '', '', '', '', '2020-11-17 20:58:41'),
(2, 'teste 2', '', '', '', '', '', '', '', '', '', '', '', '2020-11-17 21:00:11');

-- --------------------------------------------------------

--
-- Estrutura da tabela `itens_entrada`
--

CREATE TABLE `itens_entrada` (
  `id_entrada` int(11) NOT NULL,
  `cod_prod_entrada` int(11) NOT NULL,
  `prod_des_entrada` varchar(255) NOT NULL,
  `un_entrada` varchar(3) NOT NULL,
  `qtd_entrada` int(11) NOT NULL,
  `vl_init_entrada` float NOT NULL,
  `vl_total_entrada` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Extraindo dados da tabela `itens_entrada`
--

INSERT INTO `itens_entrada` (`id_entrada`, `cod_prod_entrada`, `prod_des_entrada`, `un_entrada`, `qtd_entrada`, `vl_init_entrada`, `vl_total_entrada`) VALUES
(2, 4, 'Coxinha', 'UN', 10, 5, 5),
(2, 4, 'Coxinha', 'UN', 10, 5, 5),
(1, 4, 'Coxinha', 'UN', 10, 5, 5),
(3, 4, 'Coxinha', 'UN', 10, 5, 50),
(3, 5, '1', 'UN', 10, 1, 1),
(4, 4, 'Coxinha', 'UN', 1, 5, 5),
(5, 4, 'Coxinha', 'UN', 1, 5, 5),
(5, 5, '1', 'UN', 1, 1, 1),
(6, 4, 'Coxinha', 'UN', 1, 5, 5),
(7, 4, 'Coxinha', 'UN', 1, 5, 5),
(7, 5, '1', 'UN', 1, 1, 1);

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
(48, 4, 'Coxinha', 'UN', 1, 4.5, 4.5),
(49, 4, 'Coxinha', 'UN', 1, 4.5, 4.5),
(50, 4, 'Coxinha', 'UN', 1, 4.5, 4.5),
(51, 4, 'Coxinha', 'UN', 1, 4.5, 4.5),
(52, 4, 'Coxinha', 'UN', 1, 4.5, 4.5),
(53, 4, 'Coxinha', 'UN', 1, 4.5, 4.5),
(54, 4, 'Coxinha', 'UN', 1, 4.5, 4.5),
(55, 4, 'Coxinha', 'UN', 1, 4.5, 4.5),
(56, 4, 'Coxinha', 'UN', 1, 4.5, 4.5),
(57, 4, 'Coxinha', 'UN', 1, 4.5, 4.5),
(58, 4, 'Coxinha', 'UN', 1, 4.5, 4.5),
(59, 4, 'Coxinha', 'UN', 1, 4.5, 4.5),
(59, 4, 'Coxinha', 'UN', 1, 4.5, 4.5),
(60, 4, 'Coxinha', 'UN', 1, 4.5, 4.5),
(60, 4, 'Coxinha', 'UN', 1, 4.5, 4.5),
(60, 4, 'Coxinha', 'UN', 1, 4.5, 4.5),
(61, 4, 'Coxinha', 'UN', 1, 4.5, 4.5),
(61, 4, 'Coxinha', 'UN', 1, 4.5, 4.5),
(61, 4, 'Coxinha', 'UN', 1, 4.5, 4.5),
(62, 4, 'Coxinha', 'UN', 1, 4.5, 4.5),
(62, 4, 'Coxinha', 'UN', 1, 4.5, 4.5),
(62, 4, 'Coxinha', 'UN', 1, 4.5, 4.5),
(62, 4, 'Coxinha', 'UN', 4, 4.5, 18),
(63, 4, 'Coxinha', 'UN', 1, 4.5, 4.5),
(63, 4, 'Coxinha', 'UN', 1, 4.5, 4.5),
(64, 4, 'Coxinha', 'UN', 1, 4.5, 4.5),
(65, 4, 'Coxinha', 'UN', 1, 4.5, 4.5),
(66, 4, 'Coxinha', 'UN', 1, 4.5, 4.5),
(67, 4, 'Coxinha', 'UN', 1, 4.5, 4.5),
(68, 4, 'Coxinha', 'UN', 1, 4.5, 4.5),
(69, 4, 'Coxinha', 'UN', 1, 4.5, 4.5),
(70, 4, 'Coxinha', 'UN', 1, 4.5, 4.5),
(71, 4, 'Coxinha', 'UN', 1, 4.5, 4.5),
(74, 4, 'Coxinha', 'UN', 1, 4.5, 4.5),
(75, 4, 'Coxinha', 'UN', 1, 4.5, 4.5),
(76, 4, 'Coxinha', 'UN', 1, 4.5, 4.5),
(78, 4, 'Coxinha', 'UN', 1, 4.5, 4.5),
(79, 4, 'Coxinha', 'UN', 1, 4.5, 4.5),
(80, 4, 'Coxinha', 'UN', 1, 4.5, 4.5),
(83, 4, 'Coxinha', 'UN', 1, 4.5, 4.5),
(84, 4, 'Coxinha', 'UN', 1, 4.5, 4.5),
(85, 4, 'Coxinha', 'UN', 1, 4.5, 4.5),
(86, 4, 'Coxinha', 'UN', 1, 4.5, 4.5),
(87, 4, 'Coxinha', 'UN', 1, 4.5, 4.5),
(90, 4, 'Coxinha', 'UN', 1, 4.5, 4.5),
(91, 4, 'Coxinha', 'UN', 1, 4.5, 4.5),
(92, 4, 'Coxinha', 'UN', 1, 4.5, 4.5),
(93, 4, 'Coxinha', 'UN', 1, 4.5, 4.5),
(94, 4, 'Coxinha', 'UN', 1, 4.5, 4.5),
(95, 4, 'Coxinha', 'UN', 1, 4.5, 4.5),
(96, 4, 'Coxinha', 'UN', 1, 4.5, 4.5),
(97, 4, 'Coxinha', 'UN', 1, 4.5, 4.5),
(98, 4, 'Coxinha', 'UN', 1, 5, 5),
(98, 4, 'Coxinha', 'UN', 1, 5, 5),
(99, 4, 'Coxinha', 'UN', 1, 5, 5),
(100, 4, 'Coxinha', 'UN', 1, 5, 5),
(101, 4, 'Coxinha', 'UN', 1, 5, 5),
(101, 4, 'Coxinha', 'UN', 2, 5, 10),
(102, 4, 'Coxinha', 'UN', 10, 5, 5),
(103, 4, 'Coxinha', 'UN', 1, 5, 5);

-- --------------------------------------------------------

--
-- Estrutura da tabela `log_usuario`
--

CREATE TABLE `log_usuario` (
  `nome` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estrutura da tabela `produtos`
--

CREATE TABLE `produtos` (
  `cod_produto` int(15) NOT NULL,
  `ean_produto` int(30) DEFAULT NULL,
  `nome_produto` varchar(100) NOT NULL,
  `categoria_produto` varchar(100) NOT NULL,
  `unidade_produto` varchar(255) NOT NULL,
  `descricão_produto` varchar(255) DEFAULT NULL,
  `pre_venda_produto` float(4,2) DEFAULT NULL,
  `pre_custo_produto` float(4,2) DEFAULT NULL,
  `estoque` varchar(5) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Extraindo dados da tabela `produtos`
--

INSERT INTO `produtos` (`cod_produto`, `ean_produto`, `nome_produto`, `categoria_produto`, `unidade_produto`, `descricão_produto`, `pre_venda_produto`, `pre_custo_produto`, `estoque`) VALUES
(4, 12345, 'Coxinha', 'Salgados', 'UN', '\n\n\n', 5.00, 4.50, '22'),
(5, 1, '1', 'Salgados', '', '1\n', 1.00, 1.00, '23'),
(6, 12, 'te', 'Doces', '', '10\n', 10.00, 10.00, '99'),
(7, 332, '', 'Selecione', '', '\n', 0.00, 0.00, ''),
(8, 1212, '', 'Selecione', '', '\n', 0.00, 0.00, ''),
(10, 3232, '', 'Selecione', '', '\n', 0.00, 0.00, ''),
(11, 12121, '', 'Selecione', '', '\n', 0.00, 0.00, ''),
(12, 15454, '', 'Selecione', '', '\n', 0.00, 0.00, ''),
(13, 12311, '', 'Selecione', '', '\n', 0.00, 0.00, ''),
(14, 33565, '', 'Selecione', '', '\n', 0.00, 0.00, ''),
(15, 4554545, '', 'Selecione', '', '\n', 0.00, 0.00, ''),
(16, 5555, '', 'Salgados', '', '\n', 0.00, 0.00, ''),
(17, 3333, '', 'Bebidas', '', '\n', 1.00, 2.00, ''),
(18, 6666, 'TESEW', 'Selecione', '', '\n', 2.00, 3.00, ''),
(19, 66, 'TESTE1', 'Salgados', '', '\n', 2.00, 3.00, ''),
(20, 1122, 'r4w', 'Salgados', 'UN', 'ewe\n', 1.00, 1.00, '1');

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
(4, 'MASTERCARD'),
(5, 'ELO');

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
(1003, 'debora', '89', '123'),
(1004, 'eduarda', '1111', '1');

-- --------------------------------------------------------

--
-- Estrutura da tabela `vendas`
--

CREATE TABLE `vendas` (
  `cod_pedido` int(11) NOT NULL,
  `nome_operador` varchar(255) DEFAULT NULL,
  `id_clientes` int(11) DEFAULT NULL,
  `vl_total` float NOT NULL,
  `pedido_fechado` varchar(1) NOT NULL,
  `data_create` datetime DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Extraindo dados da tabela `vendas`
--

INSERT INTO `vendas` (`cod_pedido`, `nome_operador`, `id_clientes`, `vl_total`, `pedido_fechado`, `data_create`) VALUES
(1, '0', 0, 0, '', '2020-09-12 12:25:11'),
(2, '0', 0, 4.5, '', '2020-09-12 12:29:01'),
(3, '0', 0, 9, '', '2020-09-12 12:35:40'),
(4, '0', 0, 4.5, '', '2020-09-12 12:37:00'),
(5, '0', 0, 4.5, '', '2020-09-12 12:56:33'),
(6, '0', 0, 4.5, '', '2020-09-12 12:58:30'),
(7, '0', 0, 10, '', '2020-09-12 13:02:06'),
(8, '0', 0, 50.5, '', '2020-09-12 13:20:45'),
(9, '0', 0, 5.5, '', '2020-09-12 13:26:31'),
(10, '0', 0, 5.5, '', '2020-09-12 13:28:06'),
(11, '0', 0, 5.5, '', '2020-09-12 13:31:15'),
(12, '0', 0, 4.5, 'S', '2020-09-14 18:20:39'),
(13, '0', 0, 4.5, 'N', '2020-09-14 18:34:32'),
(14, '0', 0, 4.5, 'N', '2020-09-14 19:11:53'),
(15, '0', 0, 14.5, 'S', '2020-09-14 21:07:13'),
(16, '0', 0, 20, 'S', '2020-09-14 21:08:39'),
(17, '0', 0, 19, 'S', '2020-09-14 21:12:09'),
(18, '0', 0, 9, 'S', '2020-09-15 17:58:26'),
(19, '0', 0, 4.5, 'S', '2020-09-19 11:55:37'),
(20, '0', 0, 5.5, 'N', '2020-09-19 11:57:07'),
(21, '0', 0, 14.5, 'N', '2020-09-19 12:02:19'),
(22, '0', 0, 14.5, 'N', '2020-09-19 12:05:37'),
(23, '0', 0, 14.5, 'N', '2020-09-19 12:38:02'),
(24, '0', 0, 14.5, 'N', '2020-09-19 12:40:20'),
(25, '0', 0, 14.5, 'N', '2020-09-19 12:44:54'),
(26, '0', 0, 14.5, 'N', '2020-09-19 12:47:53'),
(27, '0', 0, 0, 'N', '2020-09-23 22:07:12'),
(28, '0', 0, 0, 'N', '2020-09-23 22:07:16'),
(29, '0', 0, 0, 'N', '2020-09-23 22:07:20'),
(30, '0', 0, 0, 'N', '2020-09-23 22:07:20'),
(31, '0', 0, 0, 'N', '2020-09-23 22:07:20'),
(32, '0', 0, 0, 'N', '2020-09-23 22:07:21'),
(33, '0', 0, 4.5, 'N', '2020-09-23 22:07:31'),
(34, '0', 0, 4.5, 'N', '2020-09-23 22:12:16'),
(35, '0', 0, 9, 'N', '2020-09-23 22:13:25'),
(36, '0', 0, 4.5, 'N', '2020-09-23 22:15:46'),
(37, '0', 0, 4.5, 'N', '2020-09-23 22:16:11'),
(38, '0', 0, 4.5, 'N', '2020-09-23 22:41:21'),
(39, '0', 0, 4.5, 'N', '2020-09-23 22:42:14'),
(40, '0', 0, 4.5, 'N', '2020-09-23 22:45:09'),
(41, '0', 0, 4.5, 'N', '2020-09-23 22:45:30'),
(42, '0', 0, 4.5, 'S', '2020-09-23 22:52:11'),
(43, '0', 0, 0, 'N', '2020-09-23 22:52:18'),
(44, '0', 0, 4.5, 'S', '2020-09-23 22:53:38'),
(45, '0', 0, 0, 'N', '2020-09-23 22:53:46'),
(46, '0', 0, 4.5, 'S', '2020-09-23 22:57:40'),
(47, '0', 0, 0, 'N', '2020-09-23 22:58:27'),
(48, '0', 0, 4.5, 'S', '2020-09-23 23:02:43'),
(49, '0', 0, 4.5, 'N', '2020-09-26 09:10:40'),
(50, '0', 0, 4.5, 'N', '2020-09-26 09:14:54'),
(51, '0', 0, 4.5, 'N', '2020-09-26 09:16:24'),
(52, '0', 0, 4.5, 'N', '2020-09-26 10:41:37'),
(53, '0', 0, 4.5, 'N', '2020-09-26 10:43:25'),
(54, '0', 0, 4.5, 'N', '2020-09-26 10:45:26'),
(55, '0', 0, 4.5, 'N', '2020-09-26 10:46:41'),
(56, '0', 0, 4.5, 'N', '2020-09-26 10:50:42'),
(57, '0', 0, 4.5, 'N', '2020-09-26 10:54:56'),
(58, '0', 1, 4.5, 'N', '2020-09-26 10:56:29'),
(59, '0', 1, 9, 'N', '2020-09-26 11:43:16'),
(60, '0', 1, 13.5, 'N', '2020-09-26 11:46:57'),
(61, '0', 1, 13.5, 'N', '2020-09-26 11:48:16'),
(62, '0', 1, 31.5, 'N', '2020-09-26 11:50:24'),
(63, '0', 1, 9, 'N', '2020-09-26 12:30:00'),
(64, '0', 1, 4.5, 'N', '2020-09-26 12:32:21'),
(65, '0', 1, 4.5, 'N', '2020-09-26 12:43:40'),
(66, '0', 1, 4.5, 'N', '2020-09-26 12:45:06'),
(67, '0', 1, 4.5, 'N', '2020-09-26 12:45:57'),
(68, '0', 1, 4.5, 'N', '2020-09-26 12:53:59'),
(69, '0', 1, 4.5, 'N', '2020-09-26 13:05:23'),
(70, '0', 1, 4.5, 'N', '2020-09-26 13:09:04'),
(71, '0', 1, 4.5, 'N', '2020-09-26 13:13:30'),
(72, '0', 1, 4.5, 'N', '2020-10-05 20:44:28'),
(73, '0', 1, 4.5, 'N', '2020-10-05 20:48:09'),
(74, '0', 1, 4.5, 'N', '2020-10-05 20:53:48'),
(75, '0', 1, 4.5, 'N', '2020-10-05 20:55:41'),
(76, '0', 1, 4.5, 'N', '2020-10-05 20:59:00'),
(77, '0', 1, 4.5, 'N', '2020-10-05 21:01:01'),
(78, '0', 1, 4.5, 'N', '2020-10-05 21:14:16'),
(79, '0', 1, 4.5, 'N', '2020-10-05 21:17:01'),
(80, '0', 1, 4.5, 'N', '2020-10-05 21:21:12'),
(81, '0', 1, 4.5, 'N', '2020-10-05 21:37:13'),
(82, '0', 1, 4.5, 'N', '2020-10-05 21:38:35'),
(83, '0', 1, 4.5, 'N', '2020-10-05 21:40:25'),
(84, '0', 1, 4.5, 'N', '2020-10-05 21:41:56'),
(85, '0', 1, 4.5, 'N', '2020-10-05 21:50:03'),
(86, '0', 1, 4.5, 'N', '2020-10-05 22:11:38'),
(87, '0', 1, 4.5, 'N', '2020-10-05 22:14:42'),
(88, '0', 1, 4.5, 'N', '2020-10-06 17:48:27'),
(89, '0', 1, 4.5, 'S', '2020-10-06 17:54:06'),
(90, '0', 1, 4.5, 'N', '2020-10-06 17:57:30'),
(91, '0', 1, 4.5, 'N', '2020-10-06 17:59:48'),
(92, '0', 1, 4.5, 'N', '2020-10-06 18:02:46'),
(93, '0', 1, 4.5, 'N', '2020-10-06 18:11:13'),
(94, '0', 1, 4.5, 'N', '2020-10-10 00:04:35'),
(95, '0', 1, 4.5, 'N', '2020-10-10 00:05:23'),
(96, '0', 1, 4.5, 'S', '2020-10-16 20:52:58'),
(97, 'itamar', 0, 4.5, 'N', '2020-10-16 20:57:39'),
(98, 'itamar', 0, 10, 'N', '2020-10-23 07:43:35'),
(99, 'itamar', 1, 5, 'N', '2020-10-23 07:56:08'),
(100, 'itamar', 1, 5, 'N', '2020-10-23 08:00:03'),
(101, 'itamar', 1, 15, 'S', '2020-11-13 12:53:16'),
(102, 'itamar', 1, 5, 'N', '2020-11-18 00:24:00'),
(103, 'itamar', 1, 5, 'N', '2020-11-18 00:25:09');

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
(48, 'Selecione', 4.5),
(49, 'DINHEIRO', 4.5),
(50, 'Selecione', 4.5),
(51, 'DINHEIRO', 4.5),
(52, '{VISA CREDITO}', 4.5),
(53, 'Selecione', 4.5),
(54, '{VISA CREDITO}', 4.5),
(55, 'DINHEIRO', 4.5),
(56, 'DINHEIRO', 4.5),
(57, 'DINHEIRO', 4.5),
(58, 'DINHEIRO', 4.5),
(59, '{VISA CREDITO}', 9),
(60, 'DINHEIRO', 13.5),
(61, 'DINHEIRO', 13.5),
(62, 'DINHEIRO', 31.5),
(63, 'DINHEIRO', 4.5),
(63, '{VISA CREDITO}', 4.5),
(64, '{VISA CREDITO}', 3),
(64, '{VISA CREDITO}', 1.5),
(65, 'DINHEIRO', 4.5),
(66, '{VISA CREDITO}', 4.5),
(67, 'DINHEIRO', 4.5),
(68, 'DINHEIRO', 4.5),
(69, '{VISA CREDITO}', 4.5),
(70, 'DINHEIRO', 4.5),
(71, 'DINHEIRO', 4.5),
(72, 'DINHEIRO', 4.5),
(73, 'Selecione', 4.5),
(74, 'DINHEIRO', 4.5),
(75, 'DINHEIRO', 4.5),
(76, 'DINHEIRO', 4.5),
(77, 'DINHEIRO', 4.5),
(78, 'DINHEIRO', 4.5),
(79, 'DINHEIRO', 4.5),
(80, 'DINHEIRO', 4.5),
(81, 'DINHEIRO', 4.5),
(83, 'DINHEIRO', 4.5),
(84, 'DINHEIRO', 4.5),
(85, 'DINHEIRO', 4.5),
(86, 'DINHEIRO', 4.5),
(87, 'DINHEIRO', 4.5),
(88, '{VISA CREDITO}', 4),
(88, 'Selecione', 0.5),
(89, 'DINHEIRO', 4.5),
(90, 'DINHEIRO', 4.5),
(91, 'DINHEIRO', 4.5),
(92, 'DINHEIRO', 4.5),
(93, 'DINHEIRO', 4),
(93, 'Selecione', 0.5),
(94, '{VISA CREDITO}', 4.5),
(95, 'DINHEIRO', 4.5),
(96, 'DINHEIRO', 4.5),
(99, 'Selecione', 5),
(100, 'MASTERCARD', 5),
(101, 'MASTERCARD', 15),
(102, 'DINHEIRO', 5),
(103, 'DINHEIRO', 5);

--
-- Índices para tabelas despejadas
--

--
-- Índices para tabela `clientes`
--
ALTER TABLE `clientes`
  ADD PRIMARY KEY (`cod_cliente`);

--
-- Índices para tabela `entradanotas`
--
ALTER TABLE `entradanotas`
  ADD PRIMARY KEY (`cod_entrada`),
  ADD KEY `cod_fornecedor_ibfk_2` (`id_fornecedor`);

--
-- Índices para tabela `fornecedor`
--
ALTER TABLE `fornecedor`
  ADD PRIMARY KEY (`cod_fornecedor`);

--
-- Índices para tabela `itens_entrada`
--
ALTER TABLE `itens_entrada`
  ADD KEY `id_entrada` (`id_entrada`);

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
  MODIFY `cod_produto` int(15) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT de tabela `tipo_pag`
--
ALTER TABLE `tipo_pag`
  MODIFY `cod_pag` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de tabela `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `id` int(4) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1005;

--
-- Restrições para despejos de tabelas
--

--
-- Limitadores para a tabela `entradanotas`
--
ALTER TABLE `entradanotas`
  ADD CONSTRAINT `cod_fornecedor_ibfk_1` FOREIGN KEY (`id_fornecedor`) REFERENCES `fornecedor` (`cod_fornecedor`),
  ADD CONSTRAINT `cod_fornecedor_ibfk_2` FOREIGN KEY (`id_fornecedor`) REFERENCES `fornecedor` (`cod_fornecedor`);

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
