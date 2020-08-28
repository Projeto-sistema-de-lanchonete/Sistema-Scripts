-- Banco de dados
create database bdlanchonete;
use bdlanchonete;

-- --------------------------------------------------------
-- Estrutura das tabelas

CREATE TABLE `usuarios` (
  `id` int(4) NOT NULL,
  `nome` varchar(100) NOT NULL,
  `cpf` varchar(11) NOT NULL,
  `senha` varchar(100) NOT NULL
);

create table produtos(
cod_produto int(15) not null,
ean_produto int(30),
nome_produto varchar(100) not null,
categoria_produto varchar(100) not null,
descricão_produto varchar(255),
pre_venda_produto decimal(4,2),
pre_custo_produto decimal(4,2),
estoque varchar(5)
);

-- --------------------------------------------------------
-- chave primaria para as tabelas

ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`id`);

ALTER TABLE produtos
  ADD PRIMARY KEY (cod_produto);
  
-- --------------------------------------------------------
-- AUTO_INCREMENT das tabelas

ALTER TABLE `usuarios`
  MODIFY `id` int(4) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1000;
COMMIT;

ALTER TABLE produtos
  MODIFY cod_produto int(15) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1245678;
COMMIT;

-- --------------------------------------------------------
-- Inserindo dados nas tabelas

INSERT INTO `usuarios` (nome, cpf, senha) VALUES
('itamar', '08919673462', '1234'),
('eduardathayse', '06576933401', '4321');

INSERT INTO  produtos (ean_produto, nome_produto, categoria_produto, descricão_produto, pre_venda_produto, pre_custo_produto, estoque) VALUES
('8711253001205', 'Hamburgue', 'Lanches', 'Hamburgue carne de sol desfida', '16,00', '16,00', '5'),
('901234123457', 'Coxinha', 'Salgados', 'Coxinha de Frango', '8,00', '10,00', '10');


select * from usuarios;  

select * from produtos;

-- deletar linha da tabela  ->>  delete from usuarios where id = 1002;