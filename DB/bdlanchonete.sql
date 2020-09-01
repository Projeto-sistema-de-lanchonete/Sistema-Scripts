-- Banco de dados: `bdlanchonete`
create database bdlanchonete;
use bdlanchonete;


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
(1, 'itamar', '2020-07-06', '08919673462', '7996030', 'rua tal', '237', 'fragoso', '52130360', 'olinda', 'PE', '', '81985278547', 'itamarasa@gmail.com'),
(2, 'debora', '0000-00-00', '', '', '', '', '', '', '', 'PE', '', '', ''),
(3, 'Eduarda', '0000-00-00', '', '', '', '', '', '', '', 'PE', '', '', ''),
(4, 'Priscila', '0000-00-00', '', '', '', '', '', '', '', 'PE', '', '', ''),
(5, 'neto', '2020-07-01', '', '', '', '', '', '', '', '', '', '', ''),
(6, 'neto', '0000-00-00', '', '', '', '', '', '', '', '', '', '', ''),
(7, 'merabe', '0000-00-00', '', '', '', '', '', '', '', '', '', '', ''),
(8, '', '0000-00-00', '', '', '', '', '', '', '', '', '', '', ''),
(9, '', '2020-10-01', '', '', '', '', '', '', '', '', '', '', '');

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
(4, 12345, 'Coxinha', 'Salgados', 'ok\n', 4.50, 1.00, '50'),
(5, 1, '1', 'Salgados', '1\n', 1.00, 1.00, '1'),
(6, 12, 'te', 'Doces', '10\n', 10.00, 10.00, '10'),
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
(1000, 'itamar', '8919673462', '1234');

--
-- Índices para tabelas despejadas
--

--
-- Índices para tabela `clientes`
--
ALTER TABLE `clientes`
  ADD PRIMARY KEY (`cod_cliente`);

--
-- Índices para tabela `produtos`
--
ALTER TABLE `produtos`
  ADD PRIMARY KEY (`cod_produto`);

--
-- Índices para tabela `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `produtos`
--
ALTER TABLE `produtos`
  MODIFY `cod_produto` int(15) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;

--
-- AUTO_INCREMENT de tabela `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `id` int(4) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1003;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;